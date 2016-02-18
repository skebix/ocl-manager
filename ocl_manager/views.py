# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import os
from os.path import join

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store


class rdfQueryPower:
    """
    Esta es una clase dummy que debe ser reemplazada por FinalQuerier
    """
    pass


def index(request):
    return HttpResponse("<a href='onto'>Ver ontología</a>")


def onto_viewer(request):
    dbgraph = open_store('rdf')
    query1 = rdfQueryPower.getClassesQuery("rdfs:Resource", dbgraph)
    query2 = rdfQueryPower.getClassesQuery("kb:Administración_Pública", dbgraph)
    query3 = rdfQueryPower.getClassesQuery("kb:Cargo", dbgraph)
    query4 = rdfQueryPower.getInstancesQuery("kb:Genérica", dbgraph)
    query5 = rdfQueryPower.getDetailsQuery("kb:Roles", "kb:Descripcion", dbgraph)
    return render(request, 'ocl_manager/onto_viewer.html', {
        "query1": query1,
        "content": query2,
        "cargos": query3,
        "perfiles": query4,
        "unPerfil": query5,
    })



def open_store(identifier):
    ident = URIRef(identifier)
    store = plugin.get("SQLAlchemy", Store)(identifier=ident)
    graph = Graph(store, identifier=ident)
    uri = Literal(os.environ.get("DATABASE_URL"))
    graph.open(uri, create=False)
    return graph


def read_store(request):
    graph = open_store('rdf')

    triples = []
    for s in graph:
        triples.append(s)
    size = len(graph)

    context = {'triples': triples, 's': size}
    return render(request, 'ocl_manager/prueba.html', context)


def create_store(request):
    create_store_with_identifier('rdf')
    return HttpResponse("Creado")


def create_store_with_identifier(identifier):
    ident = URIRef(identifier)
    store = plugin.get("SQLAlchemy", Store)(identifier=ident)
    graph = Graph(store, identifier=ident)
    uri = Literal(os.environ.get("DATABASE_URL"))
    graph.open(uri, create=True)
    graph.parse(join(join(settings.BASE_DIR, 'static'), 'output.xml'))


def index(request):
    return HttpResponse("Placeholder")
