from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ServicePerson(models.Model):
    Pid = models.AutoField(null=False)
    Ppass = models.CharField(null=False,max_length=30)