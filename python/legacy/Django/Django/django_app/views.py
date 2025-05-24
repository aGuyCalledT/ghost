from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def kontakt(request):
    return render(request, "kontakt.html")

def ueber_mich(request):
    return render(request, 'ueber_mich.html')

def aktuelle_projekte(request):
    return render(request, 'aktuelle_projekte.html')

def place_holder(request):
    return render(request, "place_holder.html")