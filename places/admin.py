from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


IMAGE_MAX_WIDTH = 150
IMAGE_MAX_HEIGHT = 150


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['show_image',]

    def show_image(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />',
            url=obj.image.url,
            max_width=IMAGE_MAX_WIDTH,
            max_height=IMAGE_MAX_HEIGHT,
        )


@admin.register(Place)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('combined_info',)

    def combined_info(self, obj):
        return f"{obj.sequence_number} {obj.place}"

    combined_info.short_description = 'Порядковый номер и место'



