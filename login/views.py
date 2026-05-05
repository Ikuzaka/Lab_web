from django.shortcuts import render, redirect
from .forms import PhoneAuthenticationForm
from django.contrib.auth import login as log
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        form = PhoneAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            log(request, user)
            return redirect('/')
    else:
        form = PhoneAuthenticationForm()
    return render(request, 'login/login.html', context={'form': form})