from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    email = forms.EmailField(required=True, label='E-mail', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'
        }
    ))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        }
    ))
    first_name = forms.CharField(required=True, label='First name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First name'
        }
    ))
    last_name = forms.CharField(required=True, label='Last name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))
    address = forms.CharField(required=True, label='Address', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Address'
        }
    ))
    city = forms.CharField(required=True, label='City', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'City'
        }
    ))
    zip_code = forms.CharField(required=True, label='Zip code', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Zip code'
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'address',
            'city',
            'zip_code'
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        user.city = self.cleaned_data['city']
        user.zip_code = self.cleaned_data['zip_code']

        if commit:
            user.save()

        return user
