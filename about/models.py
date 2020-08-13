from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class AboutPage(Page):
    section_title = models.CharField(
        blank=True,
        max_length=60,
    )

    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )

    about_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        help_text='About page protrait image.',
        on_delete=models.SET_NULL,
    )

    about_section_text = models.TextField(
        blank=True,
        help_text="The about section text for the page."
    )

    content_panels = Page.content_panels + [
        FieldPanel("section_title"),
        FieldPanel("subtitle"),
        FieldPanel("about_section_text"),
        ImageChooserPanel("about_image"),
    ]
