from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Internship, Member, Suggestions, Scolarships, Hackathons, Fellowships, Certifications, Competetive
from django.http import JsonResponse, Http404

branches = ['Engineering', 'Management', 'Medical and  Para-medical', 'Humanities and Social Sciences', 'Law', 'Sciences']

@login_required
def internships(request):
    context = {
        'branches': branches,
        'count': Internship.objects.all().count(),
        'posts': Internship.objects.all()
    }
    return render(request, 'page/internships.html', context)

def about(request):
    context = {
        'members': Member.objects.all(),
        'title': 'About'
    }
    return render(request, 'page/about.html', context)

def contact_us(request):
    return render(request, 'page/contactus.html', {'title': 'SIC - ContactUs'})

def feedback(request):
    if request.method == "POST":
        if request.POST.get('suggestion'):
            sug = Suggestions()
            sug.user_name = request.user
            sug.description = request.POST.get('suggestion')
            sug.save()
    context = {
        'posts': Internship.objects.all()
    }
    return render(request, 'page/internships.html', context)

def scholarships(request):
    context = {
        'scholarships': Scolarships.objects.all()
    }
    return render(request, 'page/scholarships.html', context)

def certifications(request):
    context = {
        'certifications': Certifications.objects.all()
    }
    return render(request, 'page/certifications.html', context)

def competitive(request):
    context = {
        'competitive': Competetive.objects.all()
    }
    return render(request, 'page/competitive.html', context)

def hackathons(request):
    context = {
        'hackathons': Hackathons.objects.all()
    }
    return render(request, 'page/hackathons.html', context)

def fellowships(request):
    context = {
        'fellowships': Fellowships.objects.all()
    }
    return render(request, 'page/fellowships.html', context)

def specific_internship(request, title):
    try:
        post = Internship.objects.get(title=title)
    except post.DoesNotExist:
        raise Http404("Internship Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_internship.html', context)

def internship_branch(request, branch):
    context = {
        'count': Internship.objects.filter(branch=branch).count(),
        "posts": Internship.objects.filter(branch=branch)
    }
    return render(request, 'page/internships.html', context)