# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Blog, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BlogAdmin(admin.ModelAdmin):
    """
    Admin class for the News model.
    """
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    list_display = (
        'title',
        'user',
        'image',
        'update_date',
        'create_date',
        'status',
    )
    list_filter = (
        'title',
        'user',
        'create_date',
    )
    search_fields = (
        'title',
        'user',
        'image',
        'update_date',
        'create_date',
        'status',
    )
    list_per_page = 20


class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for the Comment model.
    """
    class Meta:
        verbose_name_plural = 'Comments'

    list_display = (
        'user',
        'blog',
        'comment_text',
        'create_date',
    )
    list_filter = (
        'user',
        'blog',
        'create_date',
    )
    search_fields = (
        'user',
        'blog',
        'comment_text',
        'create_date',
    )
    list_per_page = 20


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
