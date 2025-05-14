from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


class Computer(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('In Use', 'In Use'),
        ('Booked', 'Booked'),
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available')
    last_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')  # Customize fields to display
    search_fields = ('name',)  # Add a search bar for the 'name' field
    list_filter = ('status',)  # Add filters for the 'status' field


class UserLog(models.Model):
    STATUS_CHOICES = [
        ('Using', 'Currently Using'),
        ('Used', 'Used'),
        ('Booked', 'Booked'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_logs_ourstatus_monitor')  # Add a unique related_name
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    computer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Booked')
    booking_date = models.DateField(null=True, blank=True)
    booking_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.status} at {self.timestamp}"