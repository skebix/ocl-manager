# -*- encoding: utf-8 -*-
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


def getClassesQuery(option, graph):
    g = graph
    n = 0
    result = []
    mom_class = option
    query_classes = g.query(
        """SELECT ?x WHERE {?x rdfs:subClassOf """ + mom_class + """ .}""")
    for row in query_classes:
        result.append(row[0].partition("#")[2])
        if result[n] == mom_class:
            result.remove(mom_class)
        n += 1
    return result


def getInstancesQuery(option, graph):
    g = graph
    result = []
    mom_class = option
    query_classes = g.query(
        """SELECT ?nombre WHERE {
        ?x rdf:type """ + mom_class + """ .
        ?x kb:Denominacion_especifica ?nombre .}""")
    for row in query_classes:
        result.append(row[0])
    return result
