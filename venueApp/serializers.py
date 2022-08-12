from rest_framework import serializers
from .models import Venue, Artist, Shows


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist


class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
