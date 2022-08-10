from django.shortcuts import render
from django.http import HttpResponse
# from .models import Question
from .models import *
from .forms import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#the index page view

def index(request):
    return render(request,"index.html")

#general register view which will ask if a student or teacher

def register(request):
    return render(request,"register.html")

#student registration view 

class StudentRegisterView(View):
    
    def get(self,request):
        #creating two forms first for creatng user and second for student
        mainform = Registration()
        form = StudentRegistration()
        return render(request,'studentregister.html',{'form':form,'mainform':mainform})
    
    def post(self,request):
        #when data is submitted the student is created and saved
        form = StudentRegistration(request.POST)
        mainform = Registration(request.POST)
        if form.is_valid() and mainform.is_valid():
            messages.success(request,'Congratulations! Registered Successfully! Move on with Login')
            mainform.save()
            usr = User.objects.get(username = request.POST['username'])
            stu = form.save(commit = False)
            stu.user = usr
            stu.save()
        return render(request,'studentregister.html',{'form':form,'mainform':mainform})

#teacher registration view

class TeacherRegisterView(View):
    
    def get(self,request):
        mainform = Registration()
        form = TeacherRegistration()
        return render(request,'teacherregister.html',{'form':form,'mainform':mainform})
    
    def post(self,request):

        form = TeacherRegistration(request.POST)
        mainform = Registration(request.POST)
        if form.is_valid() and mainform.is_valid():
            messages.success(request,'Congratulations! Registered Successfully! Move on with Login')
            mainform.save()
            usr = User.objects.get(username = request.POST['username'])
            stu = form.save(commit = False)
            stu.user = usr
            stu.save()
        return render(request,'teacherregister.html',{'form':form,'mainform':mainform})

@method_decorator(login_required,name = 'dispatch')
class ProfileView(View):
    def get(self,request):
        usr = request.user
        stu = student.objects.filter(user = usr).first()
        print(stu)
        if stu is None:
            teach = teacher.objects.filter(user=usr).first()
            return render(request,'profile.html',{'data':teach,'active':'btn-primary'})
        return render(request,'profile.html',{'data':stu,'active':'btn-primary'})
