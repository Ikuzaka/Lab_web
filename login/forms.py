# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class PhoneAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Phone Number', max_length=15)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:

            from .models import MyUser
            try:
                user = MyUser.objects.get(phone_number=username)
                if user.check_password(password):
                    self.user_cache = user
                else:
                    raise ValidationError('Invalid password')
            except MyUser.DoesNotExist:
                raise ValidationError('User with this phone number does not exist')

        return self.cleaned_data