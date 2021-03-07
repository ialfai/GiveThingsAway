from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.models import User

from .models import Donation, Institution
from .forms import RegistrationForm, LoginForm

# - uruchom aplikację i zweryfikuj, czy pliki statyczne poprawnie się ładują.


class LandingPage(View):

    def get(self, request):
        bags = Donation.objects.all()
        if bags:
            bags_list = []
            for i in bags:
                bags_list.append(int(i.quantity))
            bags_number = sum(bags_list)
        else:
            bags_number = 0
        organization_number = Institution.objects.count()
        foundations = Institution.objects.filter(type=1)
        local = Institution.objects.filter(type=3)
        ngo = Institution.objects.filter(type=2)
        return render(request, 'index.html', {'bags_number': bags_number,
                                              'organization_number': organization_number,
                                              'foundations': foundations,
                                              'local': local,
                                              'ngo': ngo,
                                              })


class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': form,
                                                      'info': 'Niepoprawne dane logowania'})
        else:
            return render(request, 'login.html', {'form': form,
                                                  'info': 'Niepoprawne dane logowania1'})


class Register(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'],
                                     email=form.cleaned_data['email'],
                                     first_name=form.cleaned_data['first_name'],
                                     last_name=form.cleaned_data['last_name'])
            return redirect('/login/')
        else:
            return render(request, 'register.html', {'form': form,
                                                     'info': 'Niepoprawne dane'})





