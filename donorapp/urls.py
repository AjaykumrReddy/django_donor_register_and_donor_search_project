
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('donate/', views.donate, name='donate'),
    path('DonorRegistration/', views.donor, name='donor'),
    path('signup/', views.signup, name='signup'),
    path('SearchDonor/', views.search, name='search'),

]