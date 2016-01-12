from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('login/index.html')
    return HttpResponse(template.render(request))
def services(request):
	template = loader.get_template('login/services.html')
	return HttpResponse(template.render(request))
