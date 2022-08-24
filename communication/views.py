from django.core.paginator import Paginator
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

    def handle_exception(self, exc):
        print(exc)
        return super().handle_exception(exc)

    def post(self, request, *args, **kwargs):
        """
        Overrwriting post function for filtering and fiding suspicious events (different event, same date and close location).
        """
        updated_location = (request.data["latitude"], request.data["longitude"])
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
