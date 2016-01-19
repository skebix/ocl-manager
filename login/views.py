from django.shortcuts import render


def main(request):
    return render(request, 'login/main.html')


def services(request):
    return render(request, 'login/services.html')
