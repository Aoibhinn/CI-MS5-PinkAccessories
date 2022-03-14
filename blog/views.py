
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# Internal:
from util.util import setup_pagination
from .forms import BlogForm
from .models import Blog
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def blog_items(request):
    """
    A view to show all blog items
    The context contains the blog_items_published
    and blog_items_drafts
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the blog page.
    """
    blog_items_published = \
        Blog.objects.filter(status=1).order_by('-create_date')
    blog_items_drafts = \
        Blog.objects.filter(status=0).order_by('-create_date')

    blog_items_published = setup_pagination(blog_items_published, request, 4)
    blog_items_count = Blog.objects.filter(status=1).count()

    context = {
        'blog_items_published': blog_items_published,
        'blog_items_drafts': blog_items_drafts,
        'blog_items_count': blog_items_count
    }

    return render(request, 'blog/blog.html', context)


def manage_blog_items(request):
    """
    A view to manage all blog items
    """
    all_blog_items = Blog.objects.order_by('-create_date')

    context = {
        'blog_items': all_blog_items,
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
            return redirect('manage_blog_items')
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


@login_required
def edit_blog_item(request, blog_item_id):
    """
    A view to editing blog items
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog_item_to_edit = get_object_or_404(Blog, pk=blog_item_id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES, instance=blog_item_to_edit)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect('manage_blog_items')
        else:
            messages.error(request, 'Failed to update blog. \
                                     Please ensure the form is valid.')
    else:
        blog_form = BlogForm(instance=blog_item_to_edit)
        messages.info(request, f'You are currently editing {blog_item_to_edit.title}')

    template = 'blog/edit_blog_item.html'
    context = {
        'blog_form': blog_form,
        'blog_item': blog_item_to_edit,
    }

    return render(request, template, context)
