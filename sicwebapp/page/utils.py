from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def send_email(content):
    data = {
            'title': content.title,
            'company_org': content.comapny_org,
            'role': content.role,
            'format': content.format,
            'description': content.description,
            'registration_open': content.registration_open,
            'registration_close': content.registration_close,
            'eligibility': content.eligibility,
            'referral_link': content.referral_link,
            'date_posted': content.date_posted,
            'multibranch': content.multibranch,
            'brought_to_you_by': content.brought_to_you_by
            }
    


    ### this is almost depricated ###
    html_content = render_to_string('page/mail_template.html', {'varname':data})
    plain_message = strip_tags(html_content)
    try:
        send_mail(
            'Test Mail',
            plain_message,
            '121910317028@gitam.in',
            ['dheerudoppalapudi@gmail.com'],
            fail_silently=False,
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponseRedirect('/internships')
