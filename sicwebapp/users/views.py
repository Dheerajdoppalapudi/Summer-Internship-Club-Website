from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Event, Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# def events(request, username):
#     current_user = request.user
#     context = {
#         "user": current_user,
#         "events": Event.objects.all()
#     }
#     return render(request, 'users/events.html', context)

@login_required
def events(request):
    # current_user = request.user
    context = {
        # "user": current_user,
        "events": Event.objects.all().order_by('-date')
    }
    return render(request, 'users/events.html', context)