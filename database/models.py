# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
	
	Emp_Id=models.CharField(max_length=10)
	Dep_Id=models.CharField(max_length=30)
	Name=models.CharField(max_length=30)
	Qualification=models.TextField(max_length=50)
	Gender=models.CharField(max_length=10, default='Male')
	Salary=models.IntegerField()
	Email=models.EmailField(blank=True, verbose_name='e-mail')

	

	#def __str__(self):
	#	return "%s"%(self.Emp_Id);




