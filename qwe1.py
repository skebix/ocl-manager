"""

PRIMER PROBADOR DE QUERYS, ESTE FUNCIONA, SE DEJARA COMO BASE PARA LOS CONSIGUIENTES

"""

from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store
from rdflib.namespace import RDF, RDFS

ident = URIRef("Adm-Publi.rdfs")
store = plugin.get("SQLAlchemy", Store)(identifier=ident)
g = Graph(store, identifier=ident)
dburi = Literal('postgresql+psycopg2://skydaddy:tesis2015@localhost:5432/ocl_manager')
g.open(dburi, create=False)
#g.parse('Adm-Publi.rdfs')
#g.parse('Adm-Publi.rdf')
qres = g.query(
    """SELECT DISTINCT ?y WHERE {
    ?x rdf:type kb:Perfil_Cargo .
    ?x ?y ?z .
    }""")
n = 1
for row in qres:
    n = n + 1
    print row[0]
print n
