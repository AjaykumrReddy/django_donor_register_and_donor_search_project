from django.shortcuts import render,redirect
from .forms import DonorsForm
from .models import *
from .search import DonorFilter


# Create your views here.
def index(request):
    return render(request, 'index.html')


def donate(request):
    return render(request, 'donate.html')


def donor(request):

    form = DonorsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'donor.html', {'form': form})


def signup(request):
    return render(request, 'signup.html')


def search(request):
    donors = Donor.objects.all()
    myFilter = DonorFilter(request.GET, queryset=donors)
    donors = myFilter.qs
    context = {'myFilter': myFilter, 'donors': donors}
    return render(request, 'search.html', context)