from django.db import models
from django.urls import reverse

# Create your models here.

class Dog(models.Model):
     name = models.CharField(max_length=100)
     breed = models.CharField(max_length=100)
     description = models.TextField(max_length=250)
     age = models.IntegerField()

     def __str__(self):
         return self.name

     def get_absolute_url(self):
         return reverse('detail', kwargs={'dog_id': self.id})

class Toy(models.Model):
     name = models.CharField(max_length=50)
     color = models.CharField(max_length=20)

     def __str__(self):
         return self.name

     def get_absolute_url(self):
         return reverse('toys_detail', kwargs={'toy_id': self.id})