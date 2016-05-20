#views.py
from forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('register/completed/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render(request,
    'registration/register.html',
    variables,
    )
 
def completed(request):
    return render(request,
    'registration/completed.html',
    )
    
def profile(request):
    return render(request,'registration/profile.html')
    
def perform_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/logout/success')
    
def loggedout(request):
    return render(request,'registration/logout.html')