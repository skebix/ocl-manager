from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login
from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')


def homemade_login(request):
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


