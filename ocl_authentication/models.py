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
    graph = open_store('rdf')
    raw_choices = querylvl1("kb:Dependencias", graph)
    institution_type_choices = []
    for stuff in raw_choices:
       institution_type_choices.append((stuff, stuff))
    job_pos = models.CharField(max_length=200)
    entry_date = models.DateTimeField()
    institution_type = models.CharField(max_length=200, choices=institution_type_choices)
    institution_name = models.CharField(max_length=200)
    #ci_supervisor = models.ForeignKey()
    user_type = models.CharField(max_length=100)

