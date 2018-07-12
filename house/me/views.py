from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='accounts/login/')
def welcome_page(request):
    return render(request, 'welcome.html')
