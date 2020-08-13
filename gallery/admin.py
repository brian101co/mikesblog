from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Gallery

@modeladmin_register
class GalleryAdmin(ModelAdmin):
    model = Gallery
    menu_label = "Gallery"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False