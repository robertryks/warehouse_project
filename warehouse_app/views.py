from django.shortcuts import render, redirect

from .models import Dimension, Company
from .forms import DimensionForm, CompanyForm


def index(request):
    return render(request, 'index.html')
