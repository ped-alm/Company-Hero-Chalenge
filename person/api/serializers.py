from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from person.models import Person


class PersonSerializer(ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'rg', 'cpf', 'telephone')

    def create(self, validated_data):
        cpf = validated_data['cpf']

        if User.objects.filter(username=cpf).exists():
            raise serializers.ValidationError("cpf already registered")

        user = User.objects.create_user(username=cpf, email=validated_data['user']['email'],
                                        first_name=validated_data['user']['first_name'],
                                        last_name=validated_data['user']['last_name'])
        user.set_unusable_password()

        validated_data['user'] = user
        return Person.objects.create(**validated_data)


class PersonUpdateSerializer(ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'rg', 'telephone')

    def update(self, instance, validated_data):
        user = validated_data.get('user')
        telephone = validated_data.get('telephone')
        rg = validated_data.get('rg')

        if user:
            first_name = user.get('first_name')
            last_name = user.get('last_name')
            email = user.get('email')

            if first_name:
                instance.user.first_name = first_name
            if last_name:
                instance.user.last_name = last_name
            if email:
                instance.user.email = email

        if telephone:
            instance.telephone = telephone
        if rg:
            instance.rg = rg

        instance.user.save()
        instance.save()
        return instance
