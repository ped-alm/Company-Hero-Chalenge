from django.contrib.auth.models import User
from django.test import TestCase

from .models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(id=1, username='95558428090', email='test@mail.com',
                                        first_name='Test', last_name='Tester')
        Person.objects.create(id=1, user=user, birth_date='2020-01-01', rg='470160457',
                              cpf='95558428090', telephone='31978456512')

    def test_person_user_deletion(self):
        """User should be deleted when the person is deleted"""
        person = Person.objects.get(pk=1)
        person.delete()
        self.assertFalse(User.objects.filter(pk=1).exists())
