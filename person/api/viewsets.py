from rest_framework.viewsets import ModelViewSet

from person.models import Person
from .serializers import PersonSerializer, PersonUpdateSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return PersonUpdateSerializer
        return PersonSerializer
