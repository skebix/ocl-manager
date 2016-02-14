# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse("<a href='onto'>Ver ontología</a>")


def onto_viewer(request):
    dbgraph = models.db_starter(0)
    query1 = models.getClassesQuery("rdfs:Resource", dbgraph)
    query2 = models.getClassesQuery("kb:Administración_Pública", dbgraph)
    query3 = models.getClassesQuery("kb:Cargo", dbgraph)
    query4 = models.getInstancesQuery("kb:Perfil_Cargo", dbgraph)
    return render(request, 'login/onto_viewer.html', {
        "query1": query1,
        "content": query2,
        "cargos": query3,
        "perfiles": query4,
    })
