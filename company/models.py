from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    trading_name = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=31)
    telephone = models.CharField(max_length=31, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(
                name="company_cnpj_idx",
                fields=["cnpj"],
            )
        ]

    def __str__(self):
        return self.cnpj
