from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from company.models import Company
from employee.models import Employee
from person.models import Person


class EmployeeSerializer(ModelSerializer):
    company_id = serializers.IntegerField(source='company.id')
    person_id = serializers.IntegerField(source='person.id')

    class Meta:
        model = Employee
        fields = ('id', 'company_id', 'person_id', 'job')

    def create(self, validated_data):
        try:
            company = Company.objects.get(pk=validated_data['company']['id'])
            person = Person.objects.get(pk=validated_data['person']['id'])

            validated_data['company'] = company
            validated_data['person'] = person

            employee = Employee.objects.create(**validated_data)
        except Company.DoesNotExist:
            raise serializers.ValidationError("company not found")
        except Person.DoesNotExist:
            raise serializers.ValidationError("person not found")
        except ValidationError as error:
            raise serializers.ValidationError(error.message)

        return employee
