from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Event(models.Model):
    event_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    date = models.DateField(null=True)
    event_link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.event_name}'
