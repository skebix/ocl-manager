from __future__ import unicode_literals
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store


def db_starter(pgmaker):
    ident = URIRef('Adm-Publi.rdfs')
    store = plugin.get('SQLAlchemy', Store)(identifier=ident)
    g = Graph(store, identifier=ident)
    dburi = Literal('postgresql+psycopg2://skydaddy:tesis2015@localhost:5432/ocl_manager')
    if pgmaker == 1:
        g.open(dburi, create=True)
        g.parse('Adm-Publi.rdfs')
        g.parse('Adm-Publi.rdf')
    else:
        g.open(dburi, create=False)
    return g


