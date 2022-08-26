from geopy import distance
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import Request

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


class ListCommunicationView(generics.ListAPIView, PageNumberPagination):
    permission_classes = [AllowAny]
    serializer_class = ListCommunicationSerializer
    queryset = Communication.objects.all()


class ListCreateCommunicationView(generics.ListCreateAPIView):
    """
    View for create communication and list all communications, based on route method.
    """

    permission_classes = [AllowAny]
    serializer_class = RetrieveUpdateDestroyCommunicatrionSerializer
    queryset = Communication.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Overrwriting post function for filtering and fiding suspicious events (different event, same date and close location).
        """
        updated_location = (request.data.get("latitude"), request.data.get("longitude"))
        for location in Communication.objects.filter(
            date=request.data["date"]
        ).values_list("latitude", "longitude", "event"):
            distance_between_locations = distance.distance(
                (updated_location), (location[0], location[1])
            ).km
            if (
                distance_between_locations <= 10
                and request.data["event"] != location[2]
            ):
                request.data["suspicious"] = True
        return super().post(request, *args, **kwargs)


class ListFilteredCommunicationView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RetrieveUpdateDestroyCommunicatrionSerializer
    lookup_url_kwarg = "owner_cpf"

    def get_queryset(self):
        cpf = self.kwargs["owner_cpf"]
        print(cpf)
        queryset = Communication.objects.filter(owner_cpf__contains=cpf)
        return queryset
