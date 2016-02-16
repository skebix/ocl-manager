# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store
from rdflib.namespace import RDF, RDFS

###### SECCIÓN DE METADATA DE RDF, ES DECIR, LO ESENCIAL #####

rdfs_resource = "rdfs:Resource"
rdfs_class = "rdfs:Class"
rdfs_literal = "rdfs:Literal"
rdfs_datatype = "rdfs:Datatype"
rdf_property = "rdfs:Property"  # Esto es una instancia de rdfs:Class
rdfs_range = "rdfs:range"
rdfs_domain = "rdfs:domain"
rdf_type = "rdf:type"  # Instancia de rdf:Property
rdfs_subclassof = "rdfs:subClassOf"
rdfs_label = "rdfs:label"
rdfs_comment = "rdfs:comment"

###### FIN DE LA SECCIÓN DE METADATA DE RDF ######

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


def getInstancesQuery(option, graph):
    g = graph
    result = []
    n = 0
    mom_class = option
    query_classes = g.query(
        """SELECT DISTINCT ?x WHERE {
        ?x """ + rdf_type + """ """ + mom_class + """ .
        ?x """ + rdfs_label + """ ?y .
        } ORDER BY ?x""")
    for row in query_classes:
        result.append(row[0].partition("#")[2])
        if result[n] == mom_class:
            result.remove(mom_class)
        n += 1
    return result


def getDetailsQuery(option, graph):
    g = graph
    result = []
    mom_class = option
    query_classes = g.query(
        """SELECT DISTINCT ?y WHERE {
        ?x """ + rdf_type + """ """ + mom_class + """ .
        ?x """ + rdfs_label + """ kb:Adm-Publi_Class10000  .
        ?x """ + rdfs_range + """ ?y .
        }""")
    for row in query_classes:
        result.append(row[0].partition("#")[2])
    return result


def getClassesQuery(option, graph):
    g = graph
    n = 0
    result = []
    mom_class = option
    query_classes = g.query(
        """SELECT ?x WHERE {
        ?x rdfs:subClassOf """ + mom_class + """ .
        }""")
    for row in query_classes:
        result.append(row[0].partition("#")[2])
        if result[n] == mom_class:
            result.remove(mom_class)
        n += 1
    return result
