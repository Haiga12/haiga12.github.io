from django.shortcuts import render
from .models import Listing

# Create your views here.
def index(request):
    propertylistings = Listing.objects.all()

    return render(request, "propertylistings/index.html", {
        "propertylistings": propertylistings
    })

def listing_details(request, listing_slug):
    selectedListing = Listing.objects.get(slug=listing_slug)

    return render(request, "propertylistings/listing-details.html", {
        "listing": selectedListing
    })
