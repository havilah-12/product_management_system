from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('register/', views.register_view, name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html',
        authentication_form=LoginForm
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_add'),
    path('edit/<int:pk>/', views.product_update, name='product_edit'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
]
