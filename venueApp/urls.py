from . import views
from django.urls import path
app_name = 'venueAppUrls'


urlpatterns = [
    path('venue/', views.VenueList.as_view(), name='venuelist'),
    path('artist/', views.ArtistList.as_view(), name='Artistlist'),
    path('shows/', views.ShowsList.as_view(), name='showslist'),
    path('venuedetail/', views.VenueDetails.as_view(), name='venuedetails'),
    path('artistdetail/', views.ArtistDetails.as_view(), name='artistdetails'),
    path('showdetail/', views.ShowsDetails.as_view(), name='showsdetails'),





]
