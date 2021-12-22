from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from posts.models import Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def CommentCreateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commentator = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'comments/comment_form.html', {'form': form})


@login_required
def CommentUpdateView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/comment_update.html', {'form': form})


@login_required
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    comment.delete()
    return redirect('post-detail', pk=post.pk)
