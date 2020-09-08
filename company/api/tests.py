from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from company.models import Company
from employee.models import Employee
from person.models import Person


class CompanyViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_company_full_company(self):
        """Should return the correct full Company model when no errors are found"""
        person = Person.objects.create(id=1, user=User.objects.create_user(username='95558428090'), cpf='95558428090')
        company = Company.objects.create(id=1, name='Test', trading_name='Tester', cnpj='test', telephone='test')
        Employee.objects.create(company=company, person=person)

        response = self.client.get('/companies/1/full_company/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['id'], company.id)
        self.assertEqual(response.data['name'], company.name)
        self.assertEqual(response.data['trading_name'], company.trading_name)
        self.assertEqual(response.data['cnpj'], company.cnpj)
        self.assertEqual(response.data['telephone'], company.telephone)
        self.assertEqual(response.data['employees'], [1])
