from django.contrib import admin
from upposts.models import Post, Category, Image, Comment


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
