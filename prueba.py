__author__ = 'nessie'

from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store

# ident = URIRef("Adm-Publi.rdf")
# store = plugin.get("SQLAlchemy", Store)(identifier=ident)
# graph = Graph(store, identifier=ident)
# dburi = Literal('postgresql+psycopg2://nessie:201152925@localhost:5432/prueba')
# graph.open(dburi, create=False)
# graph.parse('Adm-Publi.rdf')

# graph.close()

ident = URIRef("Adm-Publi.rdfs")
store = plugin.get("SQLAlchemy", Store)(identifier=ident)
graph = Graph(store, identifier=ident)
dburi = Literal('postgresql+psycopg2://nessie:201152925@localhost:5432/prueba')
graph.open(dburi, create=False)

# graph.parse('Adm-Publi.rdfs')

qres = graph.query(
        """SELECT DISTINCT ?a
           WHERE {
              ?a rdf:type rdfs:Class .
              ?a rdfs:subClassOf ?b .
              ?b rdfs:label "Dependencias" .
           }""")

qres2 = graph.query(
        """SELECT DISTINCT ?x ?c
                     WHERE {
                             {
                                 { ?x a rdfs:Class }
                                 union
                                 { ?x rdfs:subClassOf ?y }
                                 union
                                 { ?z rdfs:subClassOf ?x }
                                 union
                                 { ?y rdfs:domain ?x }
                                 union
                                 { ?y rdfs:range ?x }
                             } .

                             ?x a ?c

                         FILTER(
                           !STRSTARTS(STR(?x), "http://www.w3.org/2002/07/owl")
                           && !STRSTARTS(STR(?x), "http://www.w3.org/1999/02/22-rdf-syntax-ns")
                           && !STRSTARTS(STR(?x), "http://www.w3.org/2000/01/rdf-schema")
                           && !STRSTARTS(STR(?x), "http://www.w3.org/2001/XMLSchema")
                           && !STRSTARTS(STR(?x), "http://www.w3.org/XML/1998/namespace")
                           && (!isBlank(?x))
                           ) .
                     }
                     ORDER BY  ?x
                     """
)

f = open('prueba.txt', 'w+')

for q in qres2:
    print q

f.close()
graph.close()
