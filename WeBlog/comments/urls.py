from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from . import views

urlpatterns = [
    path('post/<int:pk>/comment/new/',
         views.CommentCreateView, name='comment-create'),
    path('post/<int:pk>/comment/update/',
         views.CommentUpdateView, name='comment-update'),
    path('post/<int:pk>/comment/delete/',
         views.CommentDeleteView, name='comment-delete'),
]
