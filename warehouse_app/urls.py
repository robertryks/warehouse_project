from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('panel/', views.PanelView.as_view(), name='panel'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('companies/', views.CompanyList.as_view(), name='company-list')
]

htmx_views = [

]

urlpatterns += htmx_views
