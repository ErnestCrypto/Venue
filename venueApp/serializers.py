from rest_framework import serializers
from .models import Venue, Artist, Shows


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = '__all__'
