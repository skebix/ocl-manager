# -*- coding: utf-8 -*-
"""
QUERY WORKING TEST 2, BIG: Para encontrar la clase que mayor que engloba todo el rdf
"""
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store

ident = URIRef("Adm-Publi.rdfs")
store = plugin.get("SQLAlchemy", Store)(identifier=ident)
g = Graph(store, identifier=ident)
dburi = Literal('postgresql+psycopg2://skydaddy:tesis2015@localhost:5432/ocl_manager')
g.open(dburi, create=False)
g.parse('Adm-Publi.rdfs')
g.parse('Adm-Publi.rdf')

#seccion de queries


qres = g.query(
    """SELECT ?x
       WHERE {
          ?x rdfs:subClassOf rdfs:Resource .
       }""")
n = 0
string = []
for row in qres:
    string.append(row[0].partition("#")[2])
    print string[n]
    n = n + 1
print "--------------------------------------------------------------------"
print "--------------------------------------------------------------------"
print "--------------------------------------------------------------------"
mom_class = ""
string.remove("KB_ROOT")
mom_class = string[0]


#Seccion de substraccion de las subclases de la clase mayor

n = 0
string = []
query_classes = g.query(
    """SELECT ?x
       WHERE {
          ?x rdfs:subClassOf kb:"""+mom_class+""" .
       }""")
for row in query_classes:
    string.append(row[0].partition("#")[2])
    if string[n] == mom_class:
        string.remove(mom_class)
    print string[n]
    n = n + 1

powerful_class = string[0]
#CON ESTE QUERY OBTENEMOS PERFIL_CARGO Y PERFIL_GRUPAL
n = 0
string = []
charge_query = g.query(
    """SELECT ?x
       WHERE {
          ?x rdfs:subClassOf kb:"""+powerful_class+""" .
       }""")
print "--------------------------------------------------------------------"
print "--------------------------------------------------------------------"
for row in charge_query:
    string.append(row[0].partition("#")[2])
    print "Posicion %d del resultado: %s" % (n, string[n])
    n = n + 1
print "--------------------------------------------------------------------"
print "--------------------------------------------------------------------"
#CON ESTE QUERY OBTENEMOS LOS PERFILES DE CARGO

profiles = string[1]
n = 0
string = []
profiles_query = g.query(
    """SELECT ?x
       WHERE {
          ?x ?y kb:"""+profiles+""" .
       }""")
print "--------------------------------------------------------------------"
print "--------------------------------------------------------------------"
print len(profiles_query)
for row in profiles_query:
    print row[0]

g.close()