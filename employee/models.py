from django.core.exceptions import ValidationError
from django.db import models
from company.models import Company
from person.models import Person


class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job = models.CharField(max_length=255)

    def validate_unique(self, exclude=None):
        if self.pk is None:
            if Employee.objects.filter(person__id=self.person.id, company__id=self.company.id).exists():
                raise ValidationError("item already exists")

        super(Employee, self).validate_unique(exclude=exclude)

    def __str__(self):
        return f'{self.person.cpf}-{self.company.name}'
