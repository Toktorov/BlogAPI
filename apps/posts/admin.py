from django.contrib import admin
from apps.posts import models


class PostImageAdmin(admin.TabularInline):
    model = models.PostImage
    extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [PostImageAdmin]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Like)
