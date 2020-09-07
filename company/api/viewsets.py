from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from company.models import Company
from employee.models import Employee
from .serializers import CompanySerializer
from .serializers import CompanyUpdateSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()

    @action(methods=['get'], detail=True)
    def full_company(self, request, pk=None):
        company = self.get_object()
        serializer = CompanySerializer(company)
        employees = Employee.objects.filter(company__id=company.id)

        employee_ids = []
        for employee in employees:
            employee_ids.append(employee.id)

        result = {'employees': employee_ids}
        result.update(serializer.data)
        return Response(result)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return CompanyUpdateSerializer
        return CompanySerializer
