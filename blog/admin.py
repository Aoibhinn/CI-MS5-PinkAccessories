# # Imports
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 3rd party:
# from django.contrib import admin

# # Internal:
# from .models import Post, Comment
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# class PostAdmin(admin.ModelAdmin):
#     """
#     Admin class for the News model.
#     """
#     class Meta:
#         verbose_name = 'Post'
#         verbose_name_plural = 'Post'

#     list_display = (
#         'title',
#         'user',
#         'image',
#         'update_date',
#         'create_date',
#         'status',
#     )
#     list_filter = (
#         'title',
#         'user',
#         'create_date',
#     )
#     search_fields = (
#         'title',
#         'user',
#         'image',
#         'update_date',
#         'create_date',
#         'status',
#     )
#     list_per_page = 20


# class CommentAdmin(admin.ModelAdmin):
#     """
#     Admin class for the Comment model.
#     """
#     class Meta:
#         verbose_name_plural = 'Comments'

#     list_display = (
#         'user',
#         'post',
#         'comment_text',
#         'create_date',
#     )
#     list_filter = (
#         'user',
#         'post',
#         'create_date',
#     )
#     search_fields = (
#         'user',
#         'post',
#         'comment_text',
#         'create_date',
#     )
#     list_per_page = 20


# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)