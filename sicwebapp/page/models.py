from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    role = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, blank=False)
    registration_open = models.DateField()
    registration_close = models.DateField()
    refer_link = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'Title: {self.title} ---> {self.role}'

class Member(models.Model):
    name = models.CharField(max_length=50, blank=False)
    domain = models.CharField(max_length=70, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    email = models.EmailField(max_length = 254, blank=False)
    linked_in = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)

    def __str__(self):
        return f'Title: {self.name} ---> {self.domain}'

class Suggestions(models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    description = models.TextField()

    def __str__(self):
        return f'Title: {self.user_name} ---> {self.description}'