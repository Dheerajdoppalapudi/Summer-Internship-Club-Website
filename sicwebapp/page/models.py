from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save, pre_save

BRANCH_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Management', 'Management'),
    ('Medical and Paramedical', 'Medical and Paramedical'),
    ('Humanities and Social Sciences', 'Humanities and Social Sciences'),
    ('Law', 'Law'),
    ('Sciences', 'Sciences'),
    ('Pharmacy', 'Pharmacy'),
    ('Nursing', 'Nursing'),
    ('Everyone', 'Everyone'),
)

BROUGHT_TO_YOU_BY = (
    ('Student Internship Club', 'Student Internship Club'),
    ('GCGC', 'GCGC'),
    ('CGC Visakhapatnam', 'CGC Visakhapatnam'),
    ('CGC Hyderabad', 'CGC Hyderabad'),
    ('CGC Bengaluru', 'CGC Bengaluru')
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
    # branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, default='Everyone')
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)
    multibranch = MultiSelectField(choices=BRANCH_CHOICES, blank=True, default='Everyone')
    brought_to_you_by = models.CharField(max_length=70, choices=BROUGHT_TO_YOU_BY, blank=True, default='Student Internship Club')

    # def save(self ,*args, **kwargs):
    #     tempstr = self.multibranch
    #     for i in tempstr:
    #         tempins = self
    #         tempins.multibranch = i
    #         super(Internship,tempins).save(*args, **kwargs)

    def __str__(self):
        return f'Title: {self.title}'

# def model_created(sender, **kwargs):
#     the_instance = kwargs['instance']
#     print("this is outside", the_instance.title, the_instance.multibranch)
#     model = Internship()
#     model.branch = the_instance.multibranch
#     model.save()
#
#     if kwargs['created']:
#         print(the_instance.title)

# post_save.connect(model_created, sender=Internship)

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
    # multibranch = MultiSelectField(choices=BRANCH_CHOICES, blank=True, default='Everyone')
    referral_link = models.CharField(max_length=150, null=True)
    link_to_apply = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)

    def __str__(self):
        return f'Title: {self.name}'

class CareerFul(models.Model):
    corporate = models.CharField(max_length=75, blank=False)
    # comapny_org = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=50)
    package = models.CharField(max_length=80)
    format = models.CharField(max_length=50)
    description = models.TextField()
    registration_open = models.DateField(null=True, blank=True)
    registration_close = models.DateField()
    eligibility = models.TextField()
    referral_link = models.CharField(max_length=100, blank=False)
    # branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, default='Everyone')
    date_posted = models.DateTimeField(default=timezone.now, blank=False, editable=False)
    multibranch = MultiSelectField(choices=BRANCH_CHOICES, blank=True, default='Everyone')
    brought_to_you_by = models.CharField(max_length=70, choices=BROUGHT_TO_YOU_BY, blank=True, default='Student Internship Club')
