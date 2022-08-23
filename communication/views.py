from rest_framework import generics
from rest_framework.permissions import AllowAny

from communication.models import Communication
from communication.serializers import (
    ListCommunicationSerializer,
    RetrieveUpdateDestroyCommunicatrionSerializer,
)


class RetrieveUpdateDestroyCommunicatrionView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = RetrieveUpdateDestroyCommunicatrionSerializer
    queryset = Communication.objects.all()
    lookup_url_kwarg = "id"


class ListCommunicationView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListCommunicationSerializer
    queryset = Communication.objects.all()


class ListCreateCommunicationView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RetrieveUpdateDestroyCommunicatrionSerializer
    queryset = Communication.objects.all()
