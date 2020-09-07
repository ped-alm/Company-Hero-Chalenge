from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from employee.models import Employee
from person.models import Person
from .serializers import PersonSerializer, PersonUpdateSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()

    @action(methods=['get'], detail=True)
    def full_person(self, request, pk=None):
        person = self.get_object()
        serializer = PersonSerializer(person)
        employees = Employee.objects.filter(person__id=person.id)

        company_ids = []
        for employee in employees:
            company_ids.append(employee.company.id)

        result = {'companies': company_ids}
        result.update(serializer.data)
        return Response(result)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return PersonUpdateSerializer
        return PersonSerializer
