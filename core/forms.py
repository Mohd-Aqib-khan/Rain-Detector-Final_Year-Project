from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class SignUpForm(UserCreationForm):
    # this is not port of model that is why write it before meta class
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','id':'pass1'}),label_suffix=" ")

    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control','id':'pass2'}),label_suffix=" ")

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }
        
        widgets = {
    
<<<<<<< HEAD
            'username': forms.TextInput(attrs={'autofocus': False, 'class': 'form-control','id':'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','id':'firstname'}),
=======
            'username': forms.TextInput(attrs={'class': 'form-control','id':'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','id':'username'}),
>>>>>>> 52f75341bd7bdb4462fe4549400829bc8fc3aed7
            'last_name': forms.TextInput(attrs={'class': 'form-control','id':'lastname'}),
            'email': forms.TextInput(attrs={'class': 'form-control','id':'email'})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control outline-none'}),label_suffix=" ")

    password = forms.CharField(
        label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),label_suffix=" ")

