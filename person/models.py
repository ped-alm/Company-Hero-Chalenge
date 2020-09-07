from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=31, null=True, blank=True)
    cpf = models.CharField(max_length=31)
    telephone = models.CharField(max_length=31, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(
                name="person_cpf_idx",
                fields=["cpf"],
            )
        ]

    def __str__(self):
        return self.user.username
