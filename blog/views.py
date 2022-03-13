from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import BlogForm
from .models import Blog


def blog_items(request):
    """
    A view to show all blog items
    The context contains the blog_items_published
    and blog_items_drafts
    """

    blog_items_published = \
        Blog.objects.filter(status=1).order_by('-create_date')
    blog_items_drafts = \
        Blog.objects.filter(status=0).order_by('-create_date')

    context = {
        'blog_items_published': blog_items_published,
        'blog_items_drafts': blog_items_drafts,
    }

    return render(request, 'blog.html', context)


def manage_blog_items(request):
    """
    A view to manage all blog items
    """
    all_news_items = Blog.objects.order_by('-create_date')

    context = {
        'blog_items': all_news_items,
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


@login_required
def edit_blog_item(request, blog_item_id):
    """
    A view to editing blog items
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog_item = get_object_or_404(Blog, pk=blog_item_id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES, instance=blog_item)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, f'{blog_item.title} '
                                      f'was successfully updated')
            """return redirect(reverse('edit_blog item', 
            args=[news_item.id]))-->"""
            return redirect('manage_blog_items')
        else:
            messages.error(
                request, f'Error, {blog_item.title} \
                was not successfully updated')
    else:
        blog_form = BlogForm(instance=blog_item)
        messages.info(request, f'You are currently editing {blog_item.title}')

    template = 'edit_blog_item.html'
    context = {
        'blog_form': blog_form,
        'blog_item': blog_item,
    }

    return render(request, template, context)
