from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from person.models import Person


class PersonSerializer(ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'user', 'rg', 'cpf', 'telephone')
