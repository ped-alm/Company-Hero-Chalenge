from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from person.models import Person


class PersonViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_person_create(self):
        """Person should be created successfully when no errors are found"""
        dto = {
            "first_name": "Test",
            "last_name": "Tester",
            "email": "test@mail.com",
            "rg": "470160457",
            "cpf": "95558428090",
            "telephone": "31978456512"
        }

        response = self.client.post('/persons/', dto, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        person = Person.objects.get(cpf='95558428090')
        self.assertEqual(dto['first_name'], person.user.first_name)
        self.assertEqual(dto['last_name'], person.user.last_name)
        self.assertEqual(dto['email'], person.user.email)
        self.assertEqual(dto['rg'], person.rg)
        self.assertEqual(dto['cpf'], person.cpf)
        self.assertEqual(dto['telephone'], person.telephone)

    def test_person_create_cpf_already_registered(self):
        """An error should be returned when an already registered cpf is inserted"""
        user = User.objects.create_user(username='95558428090')
        Person.objects.create(user=user, cpf='95558428090')

        dto = {
            "first_name": "Test",
            "last_name": "Tester",
            "email": "test@mail.com",
            "cpf": "95558428090",
        }

        response = self.client.post('/persons/', dto, format='json')
        self.assertContains(response, 'person with this cpf already exists', status_code=status.HTTP_400_BAD_REQUEST)

    def test_person_update(self):
        """Person should be updated successfully when no errors are found"""
        user = User.objects.create_user(id=1, username='95558428090', email='test@mail.com',
                                        first_name='Test', last_name='Tester')
        Person.objects.create(id=1, user=user, birth_date='2020-01-01', rg='470160457',
                              cpf='95558428090', telephone='31978456512')

        dto = {
            "first_name": "Test2",
            "last_name": "Tester2",
            "email": "test@mail.com2",
            "rg": "470160458",
            "telephone": "31978456513"
        }

        response = self.client.put('/persons/1/', dto, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        person = Person.objects.get(cpf='95558428090')
        self.assertEqual(dto['first_name'], person.user.first_name)
        self.assertEqual(dto['last_name'], person.user.last_name)
        self.assertEqual(dto['email'], person.user.email)
        self.assertEqual(dto['rg'], person.rg)
        self.assertEqual(dto['telephone'], person.telephone)

    def test_person_partial_update(self):
        """Person should be partial_updated successfully when no errors are found"""
        user = User.objects.create_user(id=1, username='95558428090', email='test@mail.com',
                                        first_name='Test', last_name='Tester')
        Person.objects.create(id=1, user=user, birth_date='2020-01-01', rg='470160457',
                              cpf='95558428090', telephone='31978456512')

        dto = {
            "first_name": "Test2"
        }

        response = self.client.patch('/persons/1/', dto, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        person = Person.objects.get(cpf='95558428090')
        self.assertEqual(dto['first_name'], person.user.first_name)
