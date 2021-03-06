from django.shortcuts import render
from django.views import View
from .models import Donation, Institution

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
        return render(request, 'index.html', {'bags_number': bags_number,
                                              'organization_number': organization_number})


class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')




