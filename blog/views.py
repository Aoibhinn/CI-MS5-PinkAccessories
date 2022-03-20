# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# Internal:
from util.util import setup_pagination
from .forms import BlogForm, CommentForm
from .models import Blog, Comment

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

@login_required
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

@login_required
def delete_blog_item(request, blog_item_id):
    """
    A view to delete blog items
    Args:
        request (object): HTTP request object.
        blog_item_id: Blog item id
    Returns:
        Renders the manage blog item after deleting the blog item
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog_item = get_object_or_404(Blog, pk=blog_item_id)
    blog_item.delete()
    messages.success(request, f'{blog_item.title} Successfully Deleted')
    return redirect(reverse('manage_blog_items'))


def blog_item(request, blog_item_id):
    """
    A view to show an individual bloe item
    Args:
        request (object): HTTP request object.
        blog_item_id: Blog item id
    Returns:
        Renders the blog item page
    """
    blog_item = get_object_or_404(Blog, pk=blog_item_id)
    comments = blog_item.comments.filter(blog=blog_item_id).\
        order_by('-create_date')
    number_of_comments = comments.count()
    comments = setup_pagination(comments, request, 2)

    comment = None

    """ Adds comment to new item"""
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog_item
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment successfully posted')
            return redirect(reverse('blog_item', args=[blog_item.id]))
        else:
            messages.error(
                request, 'Comment failed to add, Please retry')
            return redirect(reverse('blog_item', args=[blog_item.id]))
    else:
        comment_form = CommentForm()

    context = {
        'blog_item': blog_item,
        'comment_form': comment_form,
        'comments': comments,
        'comment': comment,
        'number_of_comments': number_of_comments,
    }

    return render(request, 'blog/blog_item.html', context)

@login_required
def delete_comment(request, comment_id):
    """
    A view to delete news item comments
    Args:
        request (object): HTTP request object.
        comment_id: Comment id
    Returns:
        Renders the edit news item page
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'The comment was deleted')
    return redirect(reverse('blog_item', args=[comment.blog_id]))
