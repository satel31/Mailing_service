from django.contrib import admin

from apps.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'text',)
    list_filter = ('post_title', 'text',)
    search_fields = ('post_title', 'text',)
