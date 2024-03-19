from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    number_of_pets = models.IntegerField(default=0)

class Cat(models.Model):
    breed = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

class Bird(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    species = models.CharField(max_length=100)

class Dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    species = models.CharField(max_length=100)

class Exotic_animal(models.Model):
    region_of_origin = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    species = models.CharField(max_length=100)
