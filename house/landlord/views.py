from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LandlordForm

# Create your views here.


@login_required(login_url='accounts/login/')
def landlord_homepage(request):
    return render(request, 'test.html')


@login_required(login_url='/accounts/login')
def new_image(request):
    '''
    posting a new post
    '''
    current_user = request.user
    if request.method == 'POST':
        form = LandlordForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            return redirect('index')
    else:
        form = LandlordForm()
    return render(request, "profiles/new_image.html", {"form": form})
