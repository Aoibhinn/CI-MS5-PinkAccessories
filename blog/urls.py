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
    path('edit_blog_item/', views.edit_blog_item, name='edit_blog_item'),
    path('manage_blog_items/', views.manage_blog_items, name='manage_blog_items'),
]