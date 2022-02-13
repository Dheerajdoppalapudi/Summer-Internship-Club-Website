from django.db import models
from django.utils import timezone

BRANCH_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Management', 'Management'),
    ('Medical and Para-medical', 'Medical and Para-medical'),
    ('Humanities and Social Sciences', 'Humanities and Social Sciences'),
    ('Law', 'Law'),
    ('Sciences', 'Sciences'),
    ('Pharmacy', 'Pharmacy'),
    ('Nursing', 'Nursing')
)

class Internship(models.Model):
    title = models.CharField(max_length=75, blank=False)
    comapny_org = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=50, blank=False)
    format = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    registration_open = models.DateField()
    registration_close = models.DateField()
    eligibility = models.TextField()
    referral_link = models.CharField(max_length=100, blank=False)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, default='Everyone')
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)

    def __str__(self):
        return f'Title: {self.title}'

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
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)

    def __str__(self):
        return f'Title: {self.name}'

class Competetive(models.Model):
    pass

class Fellowships(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.CharField(max_length=35)
    eligibility = models.TextField()
    location_and_format = models.CharField(max_length=100)
    university_organization = models.CharField(max_length=100, null=True)
    funding = models.CharField(max_length=10, null=True)
    benifits = models.TextField()
    date_of_expiry = models.DateField()
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)
    referral_link = models.CharField(max_length=150)
    link_to_apply = models.CharField(max_length=150)

    def __str__(self):
        return f'Title: {self.name}'

class Hackathons(models.Model):
    name = models.CharField(max_length=50)
    hosted_by = models.CharField(max_length=50)
    eligibility = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    topics = models.CharField(max_length=150)
    # enter "," separated values
    format = models.CharField(max_length=50)
    prize_money_description = models.TextField(blank=True)
    link_to_apply = models.CharField(max_length=150, blank=True)
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)

    def __str__(self):
        return f'Title: {self.name}'

class Scolarships(models.Model):
    name = models.CharField(max_length=150)
    eligibility = models.CharField(max_length=150)
    description = models.TextField()
    university_organization = models.CharField(max_length=100, null=True)
    stipend = models.CharField(max_length=80)
    duration = models.CharField(max_length=80)
    end_date = models.DateField()
    country = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, default='Everyone')
    referral_link = models.CharField(max_length=150, null=True)
    link_to_apply = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)

    def __str__(self):
        return f'Title: {self.name}'