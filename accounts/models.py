# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)
	code = models.CharField(max_length=100,blank=True,null=True)

class Customer(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)
	code = models.CharField(max_length=100,blank=True,null=True)
	qualification = models.CharField(max_length=100,blank=True,null=True)

