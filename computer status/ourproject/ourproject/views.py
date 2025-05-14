from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from ourstatus_monitor.models import Computer  # Import the Computer model
from django.contrib.auth import authenticate, login

# Home Page View
def homepage(request):
    return render(request, 'home.html')  # Render the home page template

# Login View
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:  # Check if the user is an admin
                return redirect('/admin/')  # Redirect to the admin dashboard
            else:
                return redirect('/')  # Redirect to the home page for non-admin users
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')
    return render(request, 'about.html')
