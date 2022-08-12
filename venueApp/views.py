from django.shortcuts import render
from .models import Venue, Artist, Shows
from .serializers import VenueSerializer, ArtistSerializer, ShowsSerializer
from rest_framework import generics


class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ShowsList(generics.ListCreateAPIView):
    queryset = Shows.objects.all()
    serializer_class = ShowsSerializer


class VenueDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class ArtistDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ShowsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shows.objects.all()
    serializer_class = ShowsSerializer


def mine():
    return {}
