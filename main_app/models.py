from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Dog(models.Model):
     def fed_for_today(self):
         print(self.feeding_set.filter(date=date.today()).count())
         return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

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
         return reverse('toys_list')

class Feeding(models.Model):
     date = models.DateField('feeding date')
     meal = models.CharField(
         max_length=1,
         choices=MEALS,
         default=MEALS[0][0]
     )

     dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

     def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
         return f"{self.get_meal_display()} on {self.date}"
     
     class Meta:
         ordering = ['-date']