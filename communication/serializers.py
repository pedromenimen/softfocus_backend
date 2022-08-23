from rest_framework import serializers

from communication.models import Communication


class RetrieveUpdateDestroyCommunicatrionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = "__all__"


class ListCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = ["latitude", "longitude", "event", "date"]
