from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Student, Teacher  # Import your models

# Custom Admin Site to modify admin interface headers and styling
class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"  # Custom header for the admin site
    site_title = "Admin Portal"  # Custom title for the admin portal
    index_title = "Welcome to the Administration Portal"  # Title for the index page

    # Customizing the context to include a CSS file
    def each_context(self, request):
        context = super().each_context(request)
        context['css_file'] = 'admin/css/custom_admin.css'  # Include custom CSS for styling
        return context

# Instantiate the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Custom User Admin to display additional fields for the User model
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('date_joined',)  # Order users by date joined

# Unregister the default User model from the default admin site
admin.site.unregister(User)
# Register models with the custom admin site
custom_admin_site.register(User, CustomUserAdmin)  # Register the User model with the custom admin
custom_admin_site.register(Student)  # Register Student model with the custom admin site
custom_admin_site.register(Teacher)  # Register Teacher model with the custom admin site
