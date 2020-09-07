from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from person.models import Person


class PersonSerializer(ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'rg', 'cpf', 'telephone')

    def create(self, validated_data):
        cpf = validated_data['cpf']

        if User.objects.filter(username=cpf).exists():
            raise serializers.ValidationError("person already registered")

        user = User.objects.create_user(username=cpf, email=validated_data['user']['email'],
                                        first_name=validated_data['user']['first_name'],
                                        last_name=validated_data['user']['last_name'])
        user.set_unusable_password()

        validated_data['user'] = user
        return Person.objects.create(**validated_data)
