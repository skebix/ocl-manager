# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models

from ocl_manager.sparkqueries import *
from ocl_manager.views import open_store


class HomemadeUserManager(BaseUserManager):
    pass


class HomemadeUser():
    pass


class Employee(models.Model):
    institution_type_choices = []
    institution_name_choices = []
    # filler functions using sparkql queries
    graph = open_store('rdf')
    c1 = querylvl1("kb:Dependencias", graph)
    for insttype in c1:
        institution_type_choices.append((insttype, insttype))
    c2 = querylvl3("kb:Dependencias", "kb:Nombre_Dependencia", graph)
    for k in c2:
        institution_name_choices.append((k, k))
    # Variables
    job_pos = models.CharField(max_length=200)
    entry_date = models.DateTimeField()
    institution_type = models.CharField(max_length=200, choices=institution_type_choices)
    institution_name = models.CharField(max_length=300, choices=institution_name_choices)
    #ci_supervisor = models.ForeignKey()
    user_type = models.CharField(max_length=100)

