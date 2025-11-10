from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_view, name='about'),
    path('register/', views.register_view, name='register'),  # register page
    path('accounts/', include('django.contrib.auth.urls')),
    path('predict/', views.predict_view, name='predict'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('change-password/', views.change_password_view, name='change_password'),# login/logout URLs
]
