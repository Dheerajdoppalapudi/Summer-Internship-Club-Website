from django.db.models.signals import post_save
from django.dispatch import receiver
from page.models import Internship
from page.utils import send_email

@receiver(post_save, sender=Internship)
def onCreate_sendmail(sender, instance, created, **kwargs):
    if created:
        context = Internship.objects.latest('date_posted')
        print(context)
        send_email(context)
