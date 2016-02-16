# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from gestor_ocl import rdfQueryPower


def index(request):
    return HttpResponse("<a href='onto'>Ver ontología</a>")


def onto_viewer(request):
    dbgraph = rdfQueryPower.db_starter(0)
    query1 = rdfQueryPower.getClassesQuery("rdfs:Resource", dbgraph)
    query2 = rdfQueryPower.getClassesQuery("kb:Administración_Pública", dbgraph)
    query3 = rdfQueryPower.getClassesQuery("kb:Cargo", dbgraph)
    query4 = rdfQueryPower.getInstancesQuery("kb:Perfil_Cargo", dbgraph)
    query5 = rdfQueryPower.getDetailsQuery("kb:Perfil_Cargo", dbgraph)
    return render(request, 'login/onto_viewer.html', {
        "query1": query1,
        "content": query2,
        "cargos": query3,
        "perfiles": query4,
        "unPerfil": query5,
    })
