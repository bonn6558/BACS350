from django.db import models
from django.urls import reverse_lazy

class Superhero (models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    strength = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f'Name: {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('hero_list')