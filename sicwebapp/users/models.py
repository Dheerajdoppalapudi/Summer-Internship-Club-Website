from django.db import models
from django.contrib.auth.models import User

EVENT_CHOICES = (
    ('Registration Link', 'Registration Link'),
    ('Recording Link', 'Recording Link'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Event(models.Model):
    event_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    event_registration = models.CharField(max_length=50, choices=EVENT_CHOICES, default='Recording Link')
    date = models.DateField(null=True)
    event_link_OR_registration_link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.event_name}'
