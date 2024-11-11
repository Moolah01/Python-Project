# myapp/urls.py
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import user_dashboard_view, index, feature_page, student_list, register, login_view
from .admin import custom_admin_site  # Import the custom admin site

urlpatterns = [
    # Custom Admin page
    path('custom_admin/', custom_admin_site.urls, name='custom_admin'),  # Ensure the name='custom_admin' is defined

    # Home page
    path('', index, name='index'),

    # Feature page
    path('feature/', feature_page, name='feature'),

    # Student list page
    path('students/', student_list, name='student_list'),

    # User dashboard page
    path('user-dashboard/', user_dashboard_view, name='user-dashboard'),

    # User registration page
    path('register/', register, name='register'),

    # Login using custom login view
    path('login/', login_view, name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password reset views
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='myapp/password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_done.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'), name='password_reset_complete'),
]
