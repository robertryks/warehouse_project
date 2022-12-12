from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('panel/', views.PanelView.as_view(), name='panel'),
]

htmx_views = [

]

urlpatterns += htmx_views
