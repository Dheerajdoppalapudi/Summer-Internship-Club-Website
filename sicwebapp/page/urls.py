from django.urls import path
from . import views
from . import utils

urlpatterns = [
    path('internships/', views.internships, name='page-internships'),
    path('sug/', views.feedback, name='page-suggestions'),
    path('', views.about, name='page-about'),
    path('contactus/', views.contact_us, name='contact-us'),
    path('scholarships/', views.scholarships, name='page-scholarships'),
    path('certifications/', views.certifications, name='page-certifications'),
    path('competitive/', views.competitive, name='page-competitive'),
    path('hackathons/', views.hackathons, name='page-hackathons'),
    path('fellowships/', views.fellowships, name='page-fellowships'),
    path('internships/search/<int:id>', views.specific_internship, name='specific_internship'),
    path('internships/<str:branch>/', views.internship_branch, name='internship_branch'),
    path('fellowships/search/<str:name>/<str:date_posted>/', views.specific_fellowship, name='specific_fellowship'),
    path('scholarships/search/<str:name>/<str:date_posted>/', views.specific_scholarship, name='specific_scholarship'),
    path('scholarships/<str:branch>/', views.scolarship_branch, name='scholarship_branch'),
    path('hackathons/search/<str:title>/<str:date_posted>/', views.specific_hackathon, name='specific_hackathon'),
    path('archives/', views.archives, name='archives'),
    path('archives/<str:section>/', views.archives_branch, name='archives-branch'),
    path('archives/selection/result', views.try2, name='selector'),
    path('demographics/', views.stats, name='stats'),
    path('careerful/', views.Careerful, name='page-careerful'),
    path('careerful/search/<str:title>/<str:date_posted>/', views.specific_careerful, name='specific_careerful'),
    path('sendmail/', utils.send_email, name='send_mail'),
    path('internships/search/regstudents-submit/', views.userRegInter, name='regstudents-submit'),
]