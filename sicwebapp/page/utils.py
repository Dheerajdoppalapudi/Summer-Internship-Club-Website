from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    try:
        send_mail(
            'Test Mail',
            'using env variables!!!',
            '121910317028@gitam.in',
            ['dheerudoppalapudi@gmail.com'],
            fail_silently=False,
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponseRedirect('/internships')
