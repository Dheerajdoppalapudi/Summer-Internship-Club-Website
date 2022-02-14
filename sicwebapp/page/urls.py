from django.urls import path
from . import views

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
    path('internships/search/<str:title>/', views.specific_internship, name='specific_internship'),
    path('internships/<str:branch>/', views.internship_branch, name='internship_branch'),
    path('fellowships/search/<str:name>/', views.specific_fellowship, name='specific_fellowship'),
    path('scholarships/search/<str:name>/', views.specific_scholarship, name='specific_scholarship'),
    path('scholarships/<str:branch>/', views.scolarship_branch, name='scholarship_branch'),
    path('hackathons/search/<str:name>/', views.specific_hackathon, name='specific_hackathon'),
    path('archives/', views.archives, name='archives'),
    path('archives/<str:section>/', views.archives_branch, name='archives-branch'),
    path('archives/selection/result', views.try2, name='selector'),
    path('statistics', views.stats, name='stats'),
]