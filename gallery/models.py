from django.db import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wagtail.core.models import Page

class Gallery(models.Model):
    image = models.ImageField(
        upload_to='gallery/',
        blank=False,
        null=False,
    )

    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title


class GalleryPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        gallery_images = Gallery.objects.all()

        paginator = Paginator(gallery_images, 9)

        if request.GET.get('page'):
            page = int(request.GET.get('page'))
        else:
            page = None
        
        try:
            gallery_images = paginator.page(page)
        except PageNotAnInteger:
            gallery_images = paginator.page(1)
            page = 1
        except EmptyPage:
            gallery_images = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        
        context['gallery_images'] = gallery_images
        context['page_range'] = paginator.page_range
        context['num_pages'] = paginator.num_pages
        context['current_page'] = page
        return context