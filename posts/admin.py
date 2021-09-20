from django.contrib import admin

# Register your models here.
from posts.models import Image, Location


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)


class ProjectAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
