from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=31, null=True, blank=True)
    cpf = models.CharField(max_length=31)
    telephone = models.CharField(max_length=31, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.cpf
