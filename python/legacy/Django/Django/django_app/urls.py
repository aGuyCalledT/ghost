from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("kontakt/", views.kontakt, name="kontakt"),
    path("ueber_mich/", views.ueber_mich, name="ueber_mich"),
    path("aktuelle_projekte/", views.aktuelle_projekte, name="aktuelle_projekte"),
    path("place_holder/", views.place_holder, name="place_holder"),
]