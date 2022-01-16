from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Member, Suggestions
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
    return render(request, 'page/scholarships.html')

def certifications(request):
    return render(request, 'page/certifications.html')

def competitive(request):
    return render(request, 'page/competitive.html')

def hackathons(request):
    return render(request, 'page/hackathons.html')

def fellowships(request):
    return render(request, 'page/fellowships.html')