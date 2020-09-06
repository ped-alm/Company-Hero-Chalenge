from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    rg = models.CharField(max_length=31)
    cpf = models.CharField(max_length=31)
    telephone = models.CharField(max_length=31)
    email = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.cpf
