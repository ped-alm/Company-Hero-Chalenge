from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from company.models import Company
from employee.models import Employee
from person.models import Person


class PersonViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_employee_create(self):
        """Employee should be created successfully when no errors are found"""
        Company.objects.create(id=1)
        Person.objects.create(id=1, user=User.objects.create_user(username="test"))

        dto = {
            "company_id": 1,
            "person_id": 1,
            "job": "Test"
        }

        response = self.client.post('/employees/', dto, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        employee = Employee.objects.get(id=1)
        self.assertEqual(dto['company_id'], employee.company.id)
        self.assertEqual(dto['person_id'], employee.person.id)
        self.assertEqual(dto['job'], employee.job)

    def test_employee_create_absent_company(self):
        """An error should be raised when an employee is tried to be created with an absent company"""
        Person.objects.create(id=1, user=User.objects.create_user(username="test"))

        dto = {
            "company_id": 1,
            "person_id": 1,
            "job": "Test"
        }

        response = self.client.post('/employees/', dto, format='json')
        self.assertContains(response, 'company not found', status_code=status.HTTP_400_BAD_REQUEST)

    def test_employee_create_absent_person(self):
        """An error should be raised when an employee is tried to be created with an absent person"""
        Company.objects.create(id=1)

        dto = {
            "company_id": 1,
            "person_id": 1,
            "job": "Test"
        }

        response = self.client.post('/employees/', dto, format='json')
        self.assertContains(response, 'person not found', status_code=status.HTTP_400_BAD_REQUEST)

    def test_employee_create_existent_relationship(self):
        """An error should be raised when an existent employee relationship is tried to be created again"""
        company = Company.objects.create(id=1)
        person = Person.objects.create(id=1, user=User.objects.create_user(username="test"))
        Employee.objects.create(company=company, person=person)

        dto = {
            "company_id": 1,
            "person_id": 1,
            "job": "Test"
        }

        response = self.client.post('/employees/', dto, format='json')
        self.assertContains(response, 'employee relationship already exists', status_code=status.HTTP_400_BAD_REQUEST)
