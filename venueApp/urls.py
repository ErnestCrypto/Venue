from . import views
from django.urls import path
app_name = 'venueAppUrls'


urlpatterns = [
    path('venue/', views.VenueList.as_view(), name='venuelist'),
    path('artist/', views.ArtistList.as_view(), name='Artistlist'),
    path('shows/', views.ShowsList.as_view(), name='showslist'),
    path('venuedetail/<str:pk>/', views.VenueDetails.as_view(), name='venuedetails'),
    path('artistdetail/<str:pk>/',
         views.ArtistDetails.as_view(), name='artistdetails'),
    path('showdetail/<str:pk>/', views.ShowsDetails.as_view(), name='showsdetails'),





]
