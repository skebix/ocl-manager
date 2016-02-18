# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

###### SECCIÓN DE METADATA DE RDF, ES DECIR, LO ESENCIAL #####

predicados = ["rdfs:Resource", "rdfs:Class", "rdfs:Literal", "rdfs:Datatype" , "rdfs:Property", "rdfs:range", "rdfs:domain" , "rdf:type", "rdfs:subClassOf", "rdfs:label", "rdfs:comment"]

###### FIN DE LA SECCIÓN DE METADATA DE RDF ######

def getInstancesQuery(option, graph):
    g = graph
    result = []
    n = 0
    pc = 0
    mom_class = option
    query_classes = g.query(
        """SELECT DISTINCT ?nombre WHERE {
        ?x rdf:type """ + mom_class + """ .
        ?x ?nombre ?y .
        FILTER (?nombre!=rdfs:label) .
        FILTER (?nombre!=rdf:type) .
        }""")
    for row in query_classes:
        result.append(row[0].partition("#")[2])
        if result[n] == mom_class:
            result.remove(mom_class)
        n += 1
    return result


def getDetailsQuery(dad, son, graph):
    g = graph
    result = []
    bigleaf = dad
    minileaf = son
    query_classes = g.query(
        """SELECT DISTINCT ?y WHERE {
        ?x rdf:type """ + bigleaf + """ .
        ?x """ + minileaf + """ ?y .
        }""")
    for row in query_classes:
        result.append(row[0])
    return result


def getClassesQuery(option, graph):
    g = graph
    n = 0
    result = []
    mom_class = option
    query_classes = g.query(
        """SELECT ?x WHERE {
        ?x rdfs:subClassOf """ + mom_class + """ .
        FILTER (?x!=kb:KB_ROOT) .
        }""")
    for row in query_classes:
        result.append(row[0].partition("#")[2])
        if result[n] == mom_class:
            result.remove(mom_class)
        n += 1
    return result
