from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.models import User

from .models import Donation, Institution, Category
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
        user = request.user
        print(user)
        return render(request, 'index.html', {'bags_number': bags_number,
                                              'organization_number': organization_number,
                                              'foundations': foundations,
                                              'local': local,
                                              'ngo': ngo,
                                              'user': user
                                              })


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        if request.user.is_authenticated:
            user = request.user
            return render(request, 'form.html', {'user': user,
                                                 'categories': categories,
                                                 'institutions': institutions})
        else:
            return render(request, 'form.html', {'categories': categories,
                                                 'institutions': institutions})


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


class Register(FormView):
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'register.html'

    def form_valid(self, form):
        User.objects.create_user(username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password'],
                                 email=form.cleaned_data['email'],
                                 first_name=form.cleaned_data['first_name'],
                                 last_name=form.cleaned_data['last_name'])
        return super().form_valid(form)


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class Profil(View):

    def get(self, request):
        user = request.user
        donations = Donation.objects.filter(user=user)
        return render(request, 'profile.html', {'user': user,
                                                'donations': donations})


class Data(View):

    def get(self, request, result):
        result = request.GET.get('result', None)
        return JsonResponse(result)


