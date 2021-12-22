from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm  # UserDetailForm
# from .models import Profile
from posts.models import Post
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


# def edit_profile(request, pk):
#     user = get_object_or_404(pk=pk)
#     form = UserDetailForm()

#     if request.method == 'POST':
#         form = UserDetailForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             profile = form.save()
#             profile.user = request.user
#             messages.success(request, "Details saved successfully.")
#             return redirect('profile')
#     else:
#         form = UserDetailForm(instance=user)
#     return render(request, 'accounts/edit_profile.html', {'form': form})


# def profile(request, pk):
#     profile = Profile.objects.get(user=request.user)
#     posts = Post.objects.filter(author=request.user)
#     context = {
#         'profile': profile,
#         'posts': posts,
#     }
#     return render(request, 'accouts/profile.html', context)
