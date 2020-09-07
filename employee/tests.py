from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from company.models import Company
from employee.models import Employee
from person.models import Person


class EmployeeTestCase(TestCase):
    def test_employee_unique_validation(self):
        """An error should be raised when an already existing company-person
        combination employee is tried to be inserted"""
        person = Person.objects.create(id=1, user=User.objects.create_user(username="test"))
        company = Company.objects.create(id=1)
        Employee.objects.create(id=1, person=person, company=company)
        try:
            Employee.objects.create(id=2, person=person, company=company)
            self.fail("expected error not found")
        except ValidationError as e:
            self.assertEqual(e.message, 'employee relationship exists')
