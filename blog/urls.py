# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.blog_items, name='blog_items'),
    path('add_blog_item/', views.add_blog_item, name='add_blog_item'),
    path('edit_blog_item/<int:blog_item_id>/', views.edit_blog_item,
         name='edit_blog_item'),
    path('manage_blog_items/', views.manage_blog_items,
         name='manage_blog_items'),
    path('delete_blog_item/<int:blog_item_id>/', views.delete_blog_item,
         name='delete_blog_item'),
    path('<int:blog_item_id>/', views.blog_item, name='blog_item'),
    path('delete_comment/<int:comment_id>/',
         views.delete_comment, name="delete_comment"),
]