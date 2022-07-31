from django.db.models.signals import post_save
from django.dispatch import receiver
from page.models import Internship
from page.utils import send_email
import threading
from threading import active_count

@receiver(post_save, sender=Internship)
def onCreate_sendmail(sender, instance, created, **kwargs):
    if created:
        context = Internship.objects.latest('date_posted')
        threading.Thread(target=send_email, args=(context,)).start()
        # thread.start()
        # thread.join()
        # send_email(context)
        # count = active_count()
        # print("============>>", count)
