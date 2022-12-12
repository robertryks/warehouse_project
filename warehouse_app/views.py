from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class PanelView(LoginRequiredMixin, TemplateView):
    template_name = 'panel.html'
