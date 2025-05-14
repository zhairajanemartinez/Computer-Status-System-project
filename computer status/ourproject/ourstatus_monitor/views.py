from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Computer
from User_Logs.models import UserLog
from django.utils.timezone import now


def home(request):
    computers = Computer.objects.all()  # Fetch all computers from the database
    return render(request, 'home.html', {'Computers': computers})

def use_computer(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    if computer.status == 'Available':
        # Update the computer's status to "In Use" or any other status
        computer.status = 'In Use'
        computer.save()
        messages.success(request, f"You are now using the computer: {computer.name}")
    else:
        messages.error(request, f"The computer '{computer.name}' is not available.")
    return redirect('home')  # Redirect back to the home page

def use_computer_auth(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            if computer.status == 'Available':
                computer.status = 'In Use'
                computer.save()
                messages.success(request, f"You are now using the computer: {computer.name}")
                return redirect('home')
            else:
                messages.error(request, f"The computer '{computer.name}' is no longer available.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'use_computer_auth.html', {'computer': computer})


def book_computer(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)

    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')

        if computer.status == 'Available':
            # Update the computer's status to "Booked"
            computer.status = 'Booked'
            computer.save()

            # Log the booking action
            UserLog.objects.create(
                user=request.user,
                action=f"Booked the computer for {booking_date} at {booking_time}",
                computer_name=computer.name,
                status="Booked"
            )

            messages.success(request, f"You have successfully booked the computer: {computer.name} for {booking_date} at {booking_time}")
            return redirect('home')  # Redirect back to the home page
        else:
            messages.error(request, f"The computer '{computer.name}' is no longer available for booking.")

    return render(request, 'book.html', {'computer': computer})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')  # Render the login page