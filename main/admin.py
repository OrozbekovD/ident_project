from django.contrib import admin
from django.utils.safestring import mark_safe
from embed_video.admin import AdminVideoMixin

from main.models import *


class ContactWalls(admin.ModelAdmin):
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
    get_image.short_description = 'Иконка'

    list_display = ('get_image',)

    readonly_fields = ('get_image',)
    save_on_top = True

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Catalog)
admin.site.register(Hashtag)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Banner)
admin.site.register(BannerSlider)
admin.site.register(New)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Place)
admin.site.register(Info)
admin.site.register(SubInfo)
admin.site.register(LastBanner)
admin.site.register(Social)
admin.site.register(Footer)
admin.site.register(ContactWall, ContactWalls)
admin.site.register(Service)
admin.site.register(ServiceIntro)
admin.site.register(ServiceImage)
admin.site.register(About, AdminVideo)
admin.site.register(ProductImage)
admin.site.register(ProductWall)


class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductImageAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]




