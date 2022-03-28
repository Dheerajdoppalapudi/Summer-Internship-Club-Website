from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Internship, Member, Suggestions, Scolarships, Hackathons, Fellowships, Certifications, Competetive
from django.http import JsonResponse, Http404
from .forms import Dateform

branches = ['Engineering', 'Management', 'Sciences', 'Humanities and Social Sciences', 'Medical and  Para-medical', 'Law', 'Pharmacy', 'Nursing']
all_archives = ['Internships', 'Scolarships', 'Fellowships', 'Hackathons']


@login_required
def internships(request):
    if request.method == "POST":
        form_data = request.POST.get('search-bar')
        try:
            post = Internship.objects.filter(title__contains=form_data)
            context = {
                'branches': branches,
                'posts': post,
                'count': Internship.objects.filter(title__contains=form_data).count()
            }
            return render(request, 'page/internships.html', context)
        except post.DoesNotExist:
            context = {
                'branches': branches,
                'message': 'No Internship avaliable with that name.',
            }
            return render(request, 'page/internships.html', context)
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

@login_required
def contact_us(request):
    return render(request, 'page/contactus.html', {'title': 'SIC - ContactUs'})

@login_required
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

@login_required
def scholarships(request):
    context = {
        'branches': branches,
        'count': Scolarships.objects.all().count(),
        'scholarships': Scolarships.objects.order_by('-date_posted')
    }
    return render(request, 'page/scholarships.html', context)

@login_required
def certifications(request):
    context = {
        'certifications': Certifications.objects.all()
    }
    return render(request, 'page/certifications.html', context)

@login_required
def competitive(request):
    context = {
        'competitive': Competetive.objects.all()
    }
    return render(request, 'page/competitive.html', context)

@login_required
def hackathons(request):
    context = {
        'count': Hackathons.objects.all().count(),
        'hackathons': Hackathons.objects.order_by('-date_posted')
    }
    return render(request, 'page/hackathons.html', context)

@login_required
def fellowships(request):
    context = {
        'count': Fellowships.objects.all().count(),
        'fellowships': Fellowships.objects.order_by('-date_posted')
    }
    return render(request, 'page/fellowships.html', context)

@login_required
def specific_internship(request, title):
    try:
        post = Internship.objects.get(title=title)
    except post.DoesNotExist:
        raise Http404("Internship Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_internship.html', context)

@login_required
def internship_branch(request, branch):
    context = {
        'branches': branches,
        'count': Internship.objects.filter(branch=branch).count(),
        "posts": Internship.objects.filter(branch=branch).order_by('-date_posted')
    }
    return render(request, 'page/internships.html', context)

@login_required
def specific_fellowship(request, name):
    try:
        post = Fellowships.objects.get(name=name)
    except post.DoesNotExist:
        raise Http404("Fellowship Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_fellowship.html', context)

@login_required
def specific_scholarship(request, name):
    # print("================================")
    # print("function triggered")
    # print("name: ", name)
    # print("type: ", type(name))
    # print("================================")
    try:
        post = Scolarships.objects.get(name=name)
    except post.DoesNotExist:
        raise Http404("Fellowship Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_scholarship.html', context)

@login_required
def scolarship_branch(request, branch):
    context = {
        'count': Scolarships.objects.filter(branch=branch).count(),
        "scholarships": Scolarships.objects.filter(branch=branch).order_by('-date_posted')
    }
    return render(request, 'page/scholarships.html', context)

@login_required
def specific_hackathon(request, name):
    try:
        post = Hackathons.objects.get(name=name)
    except post.DoesNotExist:
        raise Http404("Hackathons Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_hackathon.html', context)

@login_required
def archives(request):
    context = {
        'allarchives': all_archives
    }
    return render(request, 'page/archives.html', context)

@login_required
def archives_branch(request, section):
    if section == "Internships":
        context = {
            'allarchives': all_archives,
            'count': Internship.objects.all().count(),
            'internships': Internship.objects.order_by('-date_posted')
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

@login_required
def try2(request):
    if request.method == "POST":
        to_date = request.POST['to-date']
        from_date = request.POST['from-date']
        selection = request.POST['selection']
        if selection == "Internship":
            #posts = Internship.objects.filter(date_posted__lte=date)
            posts = Internship.objects.filter(date_posted__range=[from_date, to_date])
            context = {
                'allarchives': all_archives,
                'internships': posts,
                'count': Internship.objects.filter(date_posted__range=[from_date, to_date]).count(),
                }
            return render(request, 'page/archives.html', context)
        elif selection == 'Scholarships':
            print("this is logging")
            posts = Scolarships.objects.filter(date_posted__range=[from_date, to_date])
            print(posts)
            context = {
                'allarchives': all_archives,
                'scholarships': posts,
                'count': Scolarships.objects.filter(date_posted__range=[from_date, to_date]).count(),
            }
            return render(request, 'page/archives.html', context)
        elif selection == 'Fellowships':
            posts = Fellowships.objects.filter(date_posted__range=[from_date, to_date])
            context = {
                'allarchives': all_archives,
                'fellowships': posts,
                'count': Fellowships.objects.filter(date_posted__range=[from_date, to_date]).count(),
            }
            return render(request, 'page/archives.html', context)
        elif selection == 'Hackathons':
            posts = Hackathons.objects.filter(date_posted__range=[from_date, to_date])
            context = {
                'allarchives': all_archives,
                'hackathons': posts,
                'count': Hackathons.objects.filter(date_posted__range=[from_date, to_date]).count(),
            }
            return render(request, 'page/archives.html', context)
    context = {
        'allarchives': all_archives
    }
    return render(request, 'page/archives.html', context)

@login_required
def stats(request):
    # internship model
    internshipsobj = []
    total_count_intern = Internship.objects.all().count()
    # internshipsobj.append(['Total Internships', total_count_intern])
    for branch in branches:
        # intern_str = "Internship "+branch+" count"
        intern_str = branch + " count"
        intern_str_val = Internship.objects.filter(branch=branch).count()
        internshipsobj.append([intern_str, intern_str_val])

    # scolarship model
    scholarshipobj = []
    total_count_scholar = Scolarships.objects.all().count()
    # scholarshipobj.append(['Total Scholarships', total_count_scholar])
    for branch in branches:
        # scolar_str = "Scolarship "+branch+" count"
        scolar_str = branch + " count"
        scolar_str_val = Scolarships.objects.filter(branch=branch).count()
        scholarshipobj.append([scolar_str, scolar_str_val])

    # hackathon model
    # for branch in branches:
    #     intern_str = "Hackathon "+branch+" count"
    #     intern_str_val = Hackathons.objects.filter(branch=branch).count()
    #     context[intern_str] = intern_str_val
    # fellowship model
    # for branch in branches:
    #     intern_str = "Fellowship "+branch+" count"
    #     intern_str_val = Fellowships.objects.filter(branch=branch).count()
    #     context[intern_str] = intern_str_val

    context = {
        'Internship_total': total_count_intern,
        'Internships': internshipsobj,
        'Scholarship_total': total_count_scholar,
        'Scolarships': scholarshipobj,
        'Hackathons': Hackathons.objects.all().count(),
        'Fellowships': Fellowships.objects.all().count(),
    }


    return render(request, 'page/stats.html', context)