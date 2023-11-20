from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:listing_slug>", views.listing_details)
]