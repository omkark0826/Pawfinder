from django.shortcuts import render
from .models import Animal

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter(status= "available")
    return render(request, "pets/animal_list.html", {"animals": animals})
