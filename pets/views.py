from django.shortcuts import render
from .models import Animal

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter(status= "available")
    return render(request, "pets/animal_list.html", {"animals": animals})

def about(request):
    return render(request, "pets/about.html")

def animal_detail(request, pk):
    animal = Animal.objects.get(pk=pk)
    return render(request, "pets/animal_detail.html", {"animal": animal})

