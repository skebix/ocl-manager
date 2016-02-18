from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')


def homemade_login(request, redirect_to):
    """
    Displays the login form and handles the login action.
    :param request: HttpRequest object
    """
    if request.user.is_authenticated():
        return render(request, 'home_page.html')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'home_page.html')
    else:
        form = AuthenticationForm(request)

    return render(request, 'registration/login.html', {'form': form})

