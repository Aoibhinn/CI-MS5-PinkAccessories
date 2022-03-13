from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import BlogForm
from .models import Blog


def blog_items(request):
    """
    A view to show all blog items
    The context contains the blog_items_published
    and blog_items_drafts
    """

    blog_items_published = Blog.objects.filter(status=1).order_by('-create_date')
    blog_items_drafts = Blog.objects.filter(status=0).order_by('-create_date')

    context = {
        'blog_items_published': blog_items_published,
        'blog_items_drafts': blog_items_drafts,
    }

    return render(request, 'blog/blog.html', context)


def manage_blog_items(request):
    """
    A view to manage all blog items
    """
    blog_items = Blog.objects.order_by('-create_date')

    context = {
        'blog_items': blog_items,
    }

    return render(request, 'blog/manage_blog_items.html', context)


@login_required
def add_blog_item(request):
    """
    A view to add a blog_item
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            form_data = blog_form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.success(request, 'Your blog item was posted successfully!')
            return redirect('blog_items')
        else:
            messages.error(
                request, 'Your blog item failed to add, Please try again')
            return redirect('add_blog_item')
    else:
        blog_form = BlogForm()

    template = 'blog/add_blog_item.html'
    context = {
        'post_form': blog_form,
    }
    return render(request, template, context)
