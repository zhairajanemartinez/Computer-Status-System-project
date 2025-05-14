from django.db import models
from django.contrib.auth.models import User

class UserLog(models.Model):
    STATUS_CHOICES = [
        ('Using', 'Currently Using'),
        ('Used', 'Used'),
        ('Booked', 'Booked'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Name or identifier of the user
    action = models.CharField(max_length=255)  # Description of the action performed
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the time and date when the log is created
    computer_name = models.CharField(max_length=100)  # Name of the computer booked or used
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Booked')  # Status of the computer

    def __str__(self):
        return f"{self.user} - {self.action} - {self.status} at {self.timestamp}"
