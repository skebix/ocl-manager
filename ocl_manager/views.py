from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store
from os.path import join

from django.contrib.auth.decorators import login_required

import os


def open_store(identifier):
    ident = URIRef(identifier)
    store = plugin.get("SQLAlchemy", Store)(identifier=ident)
    graph = Graph(store, identifier=ident)
    uri = Literal(os.environ.get("DATABASE_URL"))
    graph.open(uri, create=False)
    return graph

@login_required
def read_store(request):
    graph = open_store('rdf')

    triples = []
    for s in graph:
        triples.append(s)
    size = len(graph)

    qres = graph.query(
    """SELECT ?nombre
       WHERE {
          ?x rdf:type kb:Perfil_Cargo .
          ?x kb:Denominacion_especifica ?nombre .
       }""")

    for row in qres:
        print row

    context = {'triples': triples, 's': size}
    return render(request, 'ocl_manager/prueba.html', context)


def create_store(request):
    create_store_with_identifier("rdf")
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
