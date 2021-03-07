from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from .models import Donation, Institution
from .forms import RegistrationForm

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
        return render(request, 'login.html')


class Register(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)

    # def get(self, request):
    #     form = RegistrationForm()
    #     return render(request, 'register.html', {'form': form})
    #
    # def post(self, request):
    #     pass




