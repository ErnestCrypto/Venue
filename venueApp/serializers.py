from rest_framework import serializers
from .models import Venue, Artist, Shows


class VenueSerializer(serializers.Serializer):
    class Meta:
        model = Venue


class ArtistSerializer(serializers.Serializer):
    class Meta:
        model = Artist


class ShowsSerializer(serializers.Serializer):
    class Meta:
        model = Shows
