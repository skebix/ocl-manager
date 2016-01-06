from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenido al gestor OCL, esta es la pagina de login")
