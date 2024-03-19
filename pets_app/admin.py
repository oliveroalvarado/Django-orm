from django.contrib import admin
from .models import Cat, Dog, Exotic_animal, Owner, Bird
# Register your models here.
admin.site.register([Cat, Dog, Exotic_animal, Owner, Bird])