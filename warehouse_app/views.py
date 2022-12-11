from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from warehouse_app.models import Company


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class PanelView(TemplateView):
    template_name = 'panel.html'


class Login(LoginView):
    template_name = 'registration/login.html'


class CompanyList(ListView):
    template_name = 'companies.html'
    model = Company
    context_object_name = 'companies'

    def get_queryset(self):
        user = self.request.user
        return user.companies.all()
