from django.shortcuts import render


def index(request):
    return render(request, 'login/index.html')


def services(request):
    return render(request, 'login/services.html')
