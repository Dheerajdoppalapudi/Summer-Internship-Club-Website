from django.urls import path
from . import views

urlpatterns = [
    path('internships/', views.internships, name='page-internships'),
    path('sug/', views.feedback, name='page-suggestions'),
    path('about/', views.about, name='page-about'),
    path('contactus/', views.contact_us, name='contact-us'),
    path('scholarships/', views.scholarships, name='page-scholarships'),
    path('certifications/', views.certifications, name='page-certifications'),
    path('competitive/', views.competitive, name='page-competitive'),
    path('hackathons/', views.hackathons, name='page-hackathons'),
    path('fellowships/', views.fellowships, name='page-fellowships'),
    path('internships/search/<str:title>/', views.specific_internship, name='specific_internship'),
    path('internships/<str:branch>/', views.internship_branch, name='internship_branch'),
]