from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(form_class=LoginForm,
         template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('profile/', views.profile, name="profile"),
    # path('profile/update/', views.edit_profile, name="profile-update"),
]
