from django.contrib.auth.models import User
from django.db import models, transaction


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=31, null=True, blank=True)
    cpf = models.CharField(max_length=31, unique=True)
    telephone = models.CharField(max_length=31, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(
                name="person_cpf_idx",
                fields=["cpf"],
            )
        ]

    @transaction.atomic
    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        super(Person, self).delete(using=using, keep_parents=keep_parents)

    def __str__(self):
        return self.user.username
