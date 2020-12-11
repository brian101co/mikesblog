from django.db import models
from blog.models import BlogPage

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    lead_text = models.CharField(
        max_length=150,
        blank=True,
        help_text='Subheading text under the banner title'
    )

    button_one = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional page to link to',
        on_delete=models.SET_NULL,
    )

    button_two = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional page to link to',
        on_delete=models.SET_NULL,
    )

    button_text_one = models.CharField(
        max_length=50,
        default='See Gallery',
        blank=False,
        help_text='Button Text'
    )

    button_text_two = models.CharField(
        max_length=50,
        default='Read Blog',
        blank=False,
        help_text='Read Blog'
    )

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Banner background image',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel('button_one'),
        PageChooserPanel('button_two'),
        FieldPanel('button_text_one'),
        FieldPanel('button_text_two'),
        ImageChooserPanel('banner_background_image'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = BlogPage.objects.live().public().order_by('published_date')
        return context
