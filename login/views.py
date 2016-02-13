# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    dbgraph = models.db_starter(0)
    qres = dbgraph.query(
        """SELECT ?x
           WHERE {
              ?x rdfs:subClassOf rdfs:Resource .
           }""")
    n = 0
    string = []
    for row in qres:
        string.append(row[0].partition("#")[2])
    n = n + 1
    output = ', '.join([q for q in string])
    return HttpResponse("Las raíces del árbol ontológico son %s." % output)


def onto_viewer(request):
    return render(request, 'login/onto_viewer.html')