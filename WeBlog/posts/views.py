from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from comments.models import Comment
# from accounts.models import Profile
from .forms import PostForm
from comments.forms import CommentForm
from django.contrib import messages
from django.views.generic import FormView, UpdateView, TemplateView, CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required
def post_list(request):
    posts = Post.objects.all()
    # profile = Profile.objects.get(user=request.user)
    context = {
        'posts': posts,
        # 'profile': profile,
    }
    return render(request, 'posts/home.html', context)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post,).order_by('-commented_on')
    # profile = Profile.objects.get(user=request.user)

    context = {
        'post': post,
        'comments': comments,
        # 'profile': profile,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_update.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')
