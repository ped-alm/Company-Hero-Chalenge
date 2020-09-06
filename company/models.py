from django.db import models
from employee.models import Employee


class Company(models.Model):
    name = models.CharField(max_length=255)
    trading_name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=31)
    telephone = models.CharField(max_length=31)
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.cnpj
