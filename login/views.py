from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'login/index.html'


class ServicesView(generic.TemplateView):
    template_name = 'login/services.html'
