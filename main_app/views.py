from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Hardcoded dog objects
dogs = [
    Dog('Jasmine', 'Italian Greyhound', 'Alien dog', 3),
    Dog('Oliver', 'Pug', 'Old reliable', 10),
    Dog('Beaufort Amadeus', 'Australian Shepherd', 'Never sleeps', 0),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
