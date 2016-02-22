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
    # filler functions using sparkql queries
    graph = open_store('rdf')
    choices1 = querylvl1("kb:Dependencias", graph)
    institution_type_choices = []
    for insttype in choices1:
        institution_type_choices.append((insttype, insttype))
    choices2 = querylvl3("kb:Alcaldía", "kb:Nombre_Dependencia", graph)
    institution_name_choices = []
    for instname in choices2:
        institution_name_choices.append((instname, instname))
    # Variables
    job_pos = models.CharField(max_length=200)
    entry_date = models.DateTimeField()
    institution_type = models.CharField(max_length=200, choices=institution_type_choices)
    institution_name = models.CharField(max_length=200, choices=institution_name_choices)
    #ci_supervisor = models.ForeignKey()
    user_type = models.CharField(max_length=100)

