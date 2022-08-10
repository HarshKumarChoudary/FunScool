from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from stuteachapp.forms import *

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/',views.register,name = 'register'),
    path('profile/',views.ProfileView.as_view(),name = 'profile'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/accounts/accounts/login/'),name='logout'),
    path('register/student/',views.StudentRegisterView.as_view(),name = 'registerstudent'),
    path('register/teacher/',views.TeacherRegisterView.as_view(),name = 'registerteacher'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=loginform),name='login'),
]