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

class Certifications(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    cost = models.CharField(max_length=10)
    requirements = models.CharField(max_length=50)
    referral_link = models.CharField(max_length=150)
    #duration = models.CharField(max_length=150)
    #duration?
    date_posted = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return f'Title: {self.name}'

class Competetive(models.Model):
    pass

class Fellowships(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    # in description we can also put the provider name
    tenure = models.CharField(max_length=15)
    # tenure or duration
    eligibility = models.CharField(max_length=50)
    format = models.CharField(max_length=20)
    # online or offline(mention venue)
    date_of_expiry = models.DateField()
    date_posted = models.DateTimeField(default=timezone.now, blank=False)
    # can add another column stipend
    referral_link = models.CharField(max_length=150)

    def __str__(self):
        return f'Title: {self.name}'

class Hackathons(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    topics = models.CharField(max_length=150)
    # enter "," separated values
    hosted_by = models.CharField(max_length=50)
    application_link = models.CharField(max_length=150)
    format = models.CharField(max_length=50)
    prize_money = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return f'Title: {self.name}'

class Scolarships(models.Model):
    name = models.CharField(max_length=150)
    eligibility = models.CharField(max_length=150)
    description = models.TextField()
    stipend = models.CharField(max_length=10)
    end_date = models.DateField()
    country = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return f'Title: {self.name}'