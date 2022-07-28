from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def send_email(content):
    try:
        send_mail(
            'Test Mail',
            str(content),
            '121910317028@gitam.in',
            ['dheerudoppalapudi@gmail.com', '121910317026@gitam.in', 'Saitarun.boddu1@gmail.com', 'ddtech_gcgc@gitam.edu'],
            fail_silently=False,
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponseRedirect('/internships')
