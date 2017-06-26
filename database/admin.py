# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Employee
from django.contrib import admin

# Register your models here.

class empAdmin(admin.ModelAdmin):
	list_display=('Name','Emp_Id', 'Dep_Id')


admin.site.register(Employee, empAdmin)
