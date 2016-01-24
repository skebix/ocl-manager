from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import os
from os.path import join

from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store

def create_store(request):
    create_store_with_identifier("rdf")
    return HttpResponse("Creado")

def create_store_with_identifier(identifier):
    ident = URIRef(identifier)
    store = plugin.get("SQLAlchemy", Store)(identifier=ident)
    graph = Graph(store, identifier=ident)
    uri = Literal(os.environ.get("DATABASE_URL"))
    graph.open(uri, create=True)
    graph.parse(join(join(settings.BASE_DIR, 'static'), 'output'))

def index(request):
    return HttpResponse("Placeholder")
