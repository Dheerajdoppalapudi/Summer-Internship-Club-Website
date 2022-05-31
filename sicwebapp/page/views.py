from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Internship, Member, Suggestions, Scolarships, Hackathons, Fellowships, Certifications, Competetive, CareerFul
from django.http import JsonResponse, Http404
# from .forms import Dateform
# from datetime import date
import datetime

branches = ['Engineering', 'Management', 'Sciences', 'Humanities and Social Sciences', 'Medical and Paramedical', 'Law', 'Pharmacy', 'Nursing']
all_archives = ['Internships', 'Scolarships', 'Fellowships', 'Hackathons']


@login_required
def internships(request):
    # today = date.today()
    # d1 = today.strftime("%Y-%m-%d")
    # print("===================================")
    # print(d1)
    if request.method == "POST":
        form_data = request.POST.get('search-bar')
        try:
            post = Internship.objects.filter(title__contains=form_data)
            context = {
                'branches': branches,
                'posts': post,
                'count': post.count()
            }
            return render(request, 'page/internships.html', context)
        except post.DoesNotExist:
            context = {
                'branches': branches,
                'message': 'No Internship avaliable with that name.',
            }
            return render(request, 'page/internships.html', context)
    q_posts = Internship.objects.filter(registration_close__gte=datetime.date.today()).order_by('-date_posted')
    context = {
        'branches': branches,
        'count': q_posts.count(),
        'posts': q_posts
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
    q_post = Scolarships.objects.filter(end_date__gte=datetime.date.today()).order_by('-date_posted')
    context = {
        'branches': branches,
        'count': q_post.count(),
        'scholarships': q_post
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
    q_posts = Hackathons.objects.filter(end_date__gte=datetime.date.today()).order_by('-date_posted')
    context = {
        'count': q_posts.count(),
        'hackathons': q_posts
    }
    return render(request, 'page/hackathons.html', context)

@login_required
def fellowships(request):
    q_posts = Fellowships.objects.order_by('-date_posted')
    context = {
        'count': q_posts.count(),
        'fellowships': q_posts
    }
    return render(request, 'page/fellowships.html', context)

@login_required
def Careerful(request):
    q_posts = CareerFul.objects.filter(registration_close__gte=datetime.date.today()).order_by('-date_posted')
    context = {
        'count': q_posts.count(),
        'careerful': q_posts
    }
    return render(request, 'page/careerful.html', context)

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
def specific_careerful(request, title):
    try:
        post = CareerFul.objects.get(corporate=title)
    except post.DoesNotExist:
        raise Http404("Internship Does Not Exist")
    context = {
            "post": post
        }
    return render(request, 'page/specific_careerful.html', context)

@login_required
def internship_branch(request, branch):
    print("===========================", branch)
    # tempval = Internship.objects.filter(multibranch=branch).order_by('-date_posted')
    # print("==================: ", tempval.multibranch)
    # print(branch)
    q_post = Internship.objects.filter(multibranch__contains=branch, registration_close__gte=datetime.date.today()).order_by('-date_posted')
    context = {
        'branches': branches,
        'count': q_post.count(),
        "posts": q_post
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
    q_posts = Scolarships.objects.filter(branch=branch, end_date__gte=datetime.date.today()).order_by('-date_posted')
    context = {
        'branches': branches,
        'count': q_posts.count(),
        "scholarships": q_posts
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
    today = datetime.date.today()
    d1 = today.strftime("%Y-%m-%d")
    if section == "Internships":
        q_posts = Internship.objects.all().order_by('-date_posted')
        context = {
            'section': 'Internships',
            'allarchives': all_archives,
            'count': q_posts.count(),
            'internships': q_posts
        }
        return render(request, 'page/archives.html', context)
    elif section == 'Scolarships':
        q_posts = Scolarships.objects.all().order_by('-date_posted')
        context = {
            'section': 'Scholarships',
            'allarchives': all_archives,
            'count': q_posts.count(),
            'scholarships': q_posts
        }
        return render(request, 'page/archives.html', context)
    elif section == 'Fellowships':
        q_posts = Fellowships.objects.all().order_by('-date_posted')
        context = {
            'section': 'Fellowships',
            'allarchives': all_archives,
            'count': q_posts.count(),
            'fellowships': q_posts
        }
        return render(request, 'page/archives.html', context)
    elif section == 'Hackathons':
        q_posts = Hackathons.objects.all().order_by('-date_posted')
        context = {
            'section': 'Hackathons',
            'allarchives': all_archives,
            'count': q_posts.count(),
            'hackathons': q_posts
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
            q_posts = Internship.objects.filter(date_posted__range=[from_date, to_date])
            context = {
                'section': 'Internships',
                'allarchives': all_archives,
                'internships': q_posts,
                'count': q_posts.count(),
                }
            return render(request, 'page/archives.html', context)
        elif selection == 'Scholarships':
            print("this is logging")
            q_posts = Scolarships.objects.filter(date_posted__range=[from_date, to_date])
            print(posts)
            context = {
                'section': 'Scholarships',
                'allarchives': all_archives,
                'scholarships': q_posts,
                'count': q_posts.count(),
            }
            return render(request, 'page/archives.html', context)
        elif selection == 'Fellowships':
            q_posts = Fellowships.objects.filter(date_posted__range=[from_date, to_date])
            context = {
                'section': 'Fellowships',
                'allarchives': all_archives,
                'fellowships': q_posts,
                'count': q_posts.count(),
            }
            return render(request, 'page/archives.html', context)
        elif selection == 'Hackathons':
            q_posts = Hackathons.objects.filter(date_posted__range=[from_date, to_date])
            context = {
                'section': 'Hackathons',
                'allarchives': all_archives,
                'hackathons': q_posts,
                'count': q_posts.count(),
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
        intern_str_val = Internship.objects.filter(multibranch__contains=branch).count()
        internshipsobj.append([intern_str, intern_str_val])

    # scolarship model
    scholarshipobj = []
    total_count_scholar = Scolarships.objects.all().count()
    # scholarshipobj.append(['Total Scholarships', total_count_scholar])
    for branch in branches:
        # scolar_str = "Scolarship "+branch+" count"
        scolar_str = branch + " count"
        scolar_str_val = Scolarships.objects.filter(branch=branch).count()
        print(scolar_str, '=====>>>>', scolar_str_val)
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