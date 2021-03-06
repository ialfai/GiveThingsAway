"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GiveStuff.views import LandingPage, Login, Register, AddDonation,\
    Logout, Profil, Data, Worki

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='main'),
    path('login/', Login.as_view(), name='login'),
    path('Register/', Register.as_view(), name='register'),
    path('AddDonation/', AddDonation.as_view(), name='adddonation'),
    path('logout/', Logout.as_view()),
    path('profil/', Profil.as_view()),
    path('my_def_in_view/', Data.as_view()),
    path('liczba_workow/', Worki.as_view())


]
