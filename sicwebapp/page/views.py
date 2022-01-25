from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Internship, Member, Suggestions, Scolarships, Hackathons, Fellowships, Certifications, Competetive
from django.http import JsonResponse, Http404

branches = ['Engineering', 'Management', 'Medical and  Para-medical', 'Humanities and Social Sciences', 'Law', 'Sciences']
all_archives = ['Internships', 'Scolarships', 'Fellowships', 'Hackathons']

@login_required
def internships(request):
    context = {
        'branches': branches,
        'count': Internship.objects.all().count(),
        'posts': Internship.objects.order_by('-date_posted')
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
        'branches': branches,
        'count': Scolarships.objects.all().count(),
        'scholarships': Scolarships.objects.order_by('-date_posted')
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
        'count': Hackathons.objects.all().count(),
        'hackathons': Hackathons.objects.order_by('-date_posted')
    }
    return render(request, 'page/hackathons.html', context)

def fellowships(request):
    context = {
        'count': Fellowships.objects.all().count(),
        'fellowships': Fellowships.objects.order_by('-date_posted')
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
        'branches': branches,
        'count': Internship.objects.filter(branch=branch).count(),
        "posts": Internship.objects.filter(branch=branch).order_by('-date_posted')
    }
    return render(request, 'page/internships.html', context)

def specific_fellowship(request, name):
    try:
        post = Fellowships.objects.get(name=name)
    except post.DoesNotExist:
        raise Http404("Fellowship Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_fellowship.html', context)

def specific_scholarship(request, name):
    try:
        post = Scolarships.objects.get(name=name)
    except post.DoesNotExist:
        raise Http404("Fellowship Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_scholarship.html', context)

def scolarship_branch(request, branch):
    context = {
        'count': Scolarships.objects.filter(branch=branch).count(),
        "scholarships": Scolarships.objects.filter(branch=branch).order_by('-date_posted')
    }
    return render(request, 'page/scholarships.html', context)

def specific_hackathon(request, name):
    try:
        post = Hackathons.objects.get(name=name)
    except post.DoesNotExist:
        raise Http404("Hackathons Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_hackathon.html', context)

def archives(request):
    context = {
        'allarchives': all_archives
    }
    return render(request, 'page/archives.html', context)

def archives_branch(request, section):
    if section == "Internships":
        context = {
            'allarchives': all_archives,
            'count': Internship.objects.all().count(),
            'posts': Internship.objects.order_by('-date_posted')
        }
        return render(request, 'page/archives.html', context)
    elif section == 'Scolarships':
        context = {
            'allarchives': all_archives,
            'count': Scolarships.objects.all().count(),
            'scholarships': Scolarships.objects.order_by('-date_posted')
        }
        return render(request, 'page/archives.html', context)
    elif section == 'Fellowships':
        context = {
            'allarchives': all_archives,
            'count': Fellowships.objects.all().count(),
            'fellowships': Fellowships.objects.order_by('-date_posted')
        }
        return render(request, 'page/archives.html', context)
    elif section == 'Hackathons':
        context = {
            'allarchives': all_archives,
            'count': Hackathons.objects.all().count(),
            'hackathons': Hackathons.objects.order_by('-date_posted')
        }
        return render(request, 'page/archives.html', context)
    return render(request, 'page/archives.html', context)