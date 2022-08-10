from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import *


#general registration form

class Registration(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

#student registration form

class StudentRegistration(ModelForm):
    class Meta:
        model = student
        fields = ('name','rollno','standard','stream')
        labels = {'name':'Student Name','rollno':'Roll No.'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'rollno':forms.TextInput(attrs={'class':'form-control'}),'standard':forms.TextInput(attrs={'class':'form-control'}),'stream':forms.TextInput(attrs={'class':'form-control'})}

#Teacher registration form

class TeacherRegistration(ModelForm):
    class Meta:
        lst = [
            ('Physics','Physics'),
            ('Chemistry','Chemistry'),
            ('Social Science','Social Science'),
            ('Mathematics','Mathematics'),
            ('Biology','Biology'),
            ('Computer','Computer'),
            ('Hindi','Hindi'),
            ('English','English'),
        ]
        model = teacher
        fields = ('name','subject','phonenumber','classestaught')
        labels = {'name':'Teacher Name','subject':'Field of Interest','phonenumber':'Contact','classestaught':'Experience'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'phonenumber':forms.TextInput(attrs={'class':'form-control'}),'subject':forms.Select(choices = lst,attrs={'class':'form-control'}),'classestaught':forms.TextInput(attrs={'class':'form-control'})}

#Login Form

class loginform(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password= forms.CharField(label= _("Password"),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control','autocomplete':'current-password'}))
