from rest_framework.viewsets import ModelViewSet
from company.models import Company
from .serializers import CompanySerializer
from .serializers import CompanyUpdateSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return CompanyUpdateSerializer
        return CompanySerializer

