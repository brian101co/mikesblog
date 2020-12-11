import readtime

from django.db import models
from django.utils import timezone
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, RichTextField, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks as wagtail_blocks

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from taggit.models import TagBase, ItemBase

from streams import blocks

class BlogListPage(Page):
    ''' Blog Listing Page Model '''

    def get_context(self, request, *args, **kwargs):
        ''' Returns all Articles or filters the articles by tags using query parameters and returns the filtered list. '''
        context = super().get_context(request, *args, **kwargs)
        posts = BlogPage.objects.live().public().order_by('-published_date')

        paginator = Paginator(posts, 6)

        if request.GET.get('page'):
            page = int(request.GET.get('page'))
        else:
            page = None


        tag = request.GET.get('tag')
        if tag:
            posts = posts.filter(tags__name=tag)
            paginator = Paginator(posts, 6)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
            page = 1
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
            page = paginator.num_pages

        context['posts'] = posts
        context['page_range'] = paginator.page_range
        context['num_pages'] = paginator.num_pages
        context['current_page'] = page
        return context

class BlogTag(TagBase):
    class Meta:
        verbose_name = "blog tag"
        verbose_name_plural = "blog tags"

class TaggedBlog(ItemBase):
    tag = models.ForeignKey(
        BlogTag,
        related_name="tagged_blogs",
        on_delete=models.CASCADE,
    )

    content_object = ParentalKey(
        'blog.BlogPage',
        on_delete=models.CASCADE,
        related_name='tagged_items',
    )


class BlogPage(Page):
    post_title = models.CharField(
        blank=False,
        max_length=80,
    )

    published_date = models.DateTimeField(default=timezone.now)

    author = models.CharField(max_length=100)

    tags = ClusterTaggableManager(through=TaggedBlog, blank=True)

    summary = models.TextField(
        blank=False,
        max_length=300,
        help_text="A brief summary of the article for the post listing."
    )

    preview_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="The preview image displayed on the post listing."
    )

    internal_page_link = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text="Select and internal page to link too.",
        on_delete=models.SET_NULL,
    )

    main_content = StreamField([
        ("blockquote", blocks.BlockquoteBlock()),
        ("Richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            features=["bold", "italic", "h2", "h3", "ol", "ul", "link"]
        )),
        ("ImageAndText", blocks.ImageAndTextBlock()),
        ("Image", blocks.ImageBlock()),
        ("Centered_Image", blocks.ImageCenteredBlock()),
    ],
    null=True,
    blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel("post_title"),
        FieldPanel("published_date"),
        FieldPanel("author"),
        ImageChooserPanel("preview_image"),
        FieldPanel("summary"),
        StreamFieldPanel("main_content"),

    ]

    promote_panels = Page.promote_panels + [
        FieldPanel("tags"),
    ]

    def get_read_time(self):
        ''' Returns the read time of the HTML body '''
        string = str(self.main_content)
        result = readtime.of_html(string)
        return result

    def get_context(self, request, *args, **kwargs):
        ''' Returns all Articles or filters the articles by tags using query parameters and returns the filtered list. '''
        context = super().get_context(request, *args, **kwargs)
        post_tag_ids = self.tags.values_list('id', flat=True)
        similar_posts = BlogPage.objects.live().public().filter(tags__in=post_tag_ids).exclude(id=self.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-published_date')[:3]
        context["similar_posts"] = similar_posts
        return context

