from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from .forms import CustomUserCreationForm, LoginForm
from django.http import HttpResponse
from service_request.models import ServiceRequest
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user = request.user
    service_requests = ServiceRequest.objects.filter(user=user)
    context = {
        'service_requests': service_requests,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'gas_id': user.gas_id,
    }
    return render(request, 'profile.html', context)