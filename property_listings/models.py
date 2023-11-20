from django.db import models

# Create your models here.

class Listing(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    mainImage = models.TextField()
    secondaryImage = models.TextField()
    description = models.TextField()
    maxGuests = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    slug = models.SlugField(unique=True)