from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import Student
from .forms import RegisterForm

# Home page
def index(request):
    return render(request, "myapp/index.html", {})

# Feature page
def feature_page(request):
    return render(request, 'myapp/Feature.html')

# Student list
def student_list(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_list.html', {'students': students})

# User dashboard view (requires login)
@login_required
def user_dashboard_view(request):
    return render(request, 'myapp/user_dashboard.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            # Redirect based on user role (admin or regular user)
            if user.is_superuser:
                return redirect('/admin/')  # Redirect to admin page if user is an admin
            else:
                return redirect('user-dashboard')  # Redirect to user dashboard for regular users
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

# Login view with error message
def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on whether the user is an admin or a regular user
                if user.is_superuser:
                    return redirect('/custom_admin/')
                else:
                    return redirect('user-dashboard')  # Redirect to user dashboard for regular users
            else:
                error_message = "Incorrect username or password."
        else:
            error_message = "Incorrect username or password."  # Message for invalid form

    else:
        form = AuthenticationForm()

    return render(request, 'myapp/login.html', {'form': form, 'error_message': error_message})

# Dashboard view (for logged-in users)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
