from django.shortcuts import render, redirect
from django.core.cache import cache
from login.admin import UserCreationForm
import random
import requests
from django.conf import settings
from django.contrib.auth import login

def registration(request):
    if request.method == 'POST':
        form = request.POST
        request.session['form'] = form
        telegram_code = ''.join(random.choices('0123456789', k=6))
        phone_number = request.POST.get('phone_number')
        request.session['phone_number'] = phone_number
        cache.set(f'telegram_code_{phone_number}', telegram_code, timeout=120)
        response = requests.post('https://gate.smsaero.ru/v2/telegram/send',
                                    auth=(settings.SMS_AERO_EMAIL, settings.SMS_AERO_API_KEY),
                                    data={
                                        'number': phone_number[1:],
                                        'code': telegram_code
                                    })
        print(response.json())
        return redirect('registration:verification_phone')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', context={'form': form})

def verify_phone_number(request):
    if request.method == 'POST':
        telegram_code = request.POST.get('verification_code')
        phone_number = request.session.get('phone_number')
        telegram_code_real = cache.get(f'telegram_code_{phone_number}', '')
        form = request.session.get('form')
        if telegram_code == telegram_code_real:
            form = UserCreationForm(form)
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'registration/verification_phone.html')