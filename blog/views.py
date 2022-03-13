# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render

# Internal:
from .models import Blog
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def blog_items(request):
    """
    Blog item view
    """
    blog_items_published = \
        Blog.objects.filter(status=1).order_by('-create_date')
    blog_items_drafts = \
        Blog.objects.filter(status=0).order_by('-create_date')

    context = {
        'blog_items_published': blog_items_published,
        'blog_items_drafts': blog_items_drafts,
    }

    return render(request, 'blog/blog.html', context)
