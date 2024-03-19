from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
@login_required
def make_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST,request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('profile')
    else:
        form = ServiceRequestForm()
    return render(request, 'make_service_request.html', {'form': form})