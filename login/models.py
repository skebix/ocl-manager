from __future__ import unicode_literals
from django.db import models
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store


def db_starter():
    ident = URIRef('Adm-Publi.rdfs')
    store = plugin.get('SQLAlchemy', Store)(identifier=ident)
    g = Graph(store, identifier=ident)
    dburi = Literal('postgresql+psycopg2://skydaddy:tesis2015@localhost:5432/ocl_manager')
    g.open(dburi, create=False)
    return g


