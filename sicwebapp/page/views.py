from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Member, Suggestions, Scolarships, Hackathons, Fellowships, Certifications, Competetive
from django.http import JsonResponse

@login_required
def internships(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'page/home.html', context)

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
        'posts': Post.objects.all()
    }
    return render(request, 'page/home.html', context)

def scholarships(request):
    context = {
        'posts': Scolarships.objects.all()
    }
    return render(request, 'page/scholarships.html', context)

def certifications(request):
    context = {
        'posts': Certifications.objects.all()
    }
    return render(request, 'page/certifications.html', context)

def competitive(request):
    context = {
        'posts': Competetive.objects.all()
    }
    return render(request, 'page/competitive.html', context)

def hackathons(request):
    context = {
        'posts': Hackathons.objects.all()
    }
    return render(request, 'page/hackathons.html', context)

def fellowships(request):
    context = {
        'posts': Fellowships.objects.all()
    }
    return render(request, 'page/fellowships.html', context)