from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Forum, Comment
from .forms import CommentForm, AddForumForm


def view_forum(request):
    """ Returns forum.html """
    template = 'forum/forum.html'
    context = {
        'forum': Forum.objects.all()
    }
    return render(request, template, context)


@login_required
def forum_comments(request, forum_id):
    """ Returns forum_comments.html """
    forum = get_object_or_404(Forum, pk=forum_id)
    comments = forum.comments.filter()
    new_comment = None
    template = 'forum/forum_comments.html'

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            """ Create Comment """
            new_comment = comment_form.save(commit=False)
            """ Assign Author To Comment """
            new_comment.comment_author = request.user
            new_comment.save()
            """ Assign Comment to Forum """
            new_comment.forum_id = forum
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, 'Successfully posted your comment.')
            return redirect(reverse('forum_comments', args=[forum.id]))
    else:
        comment_form = CommentForm()

    context = {
        'forum': forum,
        'comments': comments,
        'comment_form': comment_form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    """ Edit Comment """
    """ Prefill Form """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.comment_author or request.user.is_superuser:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(request, 'Comment successfully updated')
                return redirect(reverse('forum' ))
            else:
                messages.error(request,
                               'Error - Please check form is valid and \
                                    try again.')
        else:
            comment_form = CommentForm(instance=comment)
            messages.info(request, f'You are editing {comment.comment_title}')
    else:
        messages.error(request, 'Sorry, only the comment author can do that')
        return redirect(reverse('home'))

    template = 'forum/edit_comment.html'
    context = {
        'comment_form': comment_form,
        'comment': comment,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.comment_author or request.user.is_superuser:
        """ Delete Comment """
        comment.delete()
        messages.success(request, 'Comment deleted')
        return redirect(reverse('forum'))
    else:
        messages.error(request, 'Sorry, only the comment author can do that')
        return redirect(reverse('home'))


@login_required
def add_forum(request):
    """ Superuser Access Only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, owners only function')
        return redirect(reverse('home'))
    """ Add Forum """
    if request.method == 'POST':
        add_forum_form = AddForumForm(request.POST, request.FILES)
        if add_forum_form.is_valid():
            new_forum = add_forum_form.save(commit=False)
            """ Assign Creator To Forum """
            new_forum.forum_creator = request.user
            new_forum.save()
            add_forum_form = AddForumForm()
            messages.success(request, 'Forum successfully added')
            return redirect(reverse('forum_comments', args=[new_forum.id]))
        else:
            messages.error(request,
                           'Error - Please check form is valid and try again.')
    else:
        add_forum_form = AddForumForm()

    template = 'forum/add_forum.html'
    context = {
        'add_forum_form': add_forum_form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def edit_forum(request, forum_id):
    """ Superuser Access Only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, owners only function')
        return redirect(reverse('home'))
    """ Edit Forum """
    """ Prefill Form """
    forum = get_object_or_404(Forum, pk=forum_id)
    if request.method == 'POST':
        add_forum_form = AddForumForm(request.POST, request.FILES, instance=forum)
        if add_forum_form.is_valid():
            add_forum_form.save()
            messages.success(request, 'Forum successfully updated')
            return redirect(reverse('forum_comments', args=[forum.id]))
        else:
            messages.error(request,
                           'Error - Please check form is valid and try again.')
    else:
        add_forum_form = AddForumForm(instance=forum)
        messages.info(request, f'You are editing {forum.forum_name}')

    template = 'forum/edit_forum.html'
    context = {
        'add_forum_form': add_forum_form,
        'forum': forum,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def delete_forum(request, forum_id):
    """ Superuser Access Only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, owners only function')
        return redirect(reverse('home'))
    """ Delete Forum """
    forum = get_object_or_404(Forum, pk=forum_id)
    forum.delete()
    messages.success(request, 'Forum deleted')
    return redirect(reverse('forum'))
