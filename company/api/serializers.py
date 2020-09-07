from rest_framework.serializers import ModelSerializer
from company.models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'trading_name', 'cnpj', 'telephone')


class CompanyUpdateSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'trading_name', 'telephone')
