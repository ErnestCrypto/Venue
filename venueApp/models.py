from django.db import models

# Creating our Venue models


class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()


# Creating our Artist models
class Artist(models.Model):
    venue = models.ForeignKey(
        Venue, related_name='venue', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)


# Creating our Shows models
class Shows(models.Model):
    artist = models.ForeignKey(
        Artist, related_name="artist", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
