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


class Chapter(models.Model):
    book = models.CharField(max_length=200)
    order = models.IntegerField()
    title = models.CharField(max_length=200)

    def export_record(self):
        return [self.book, self.order, self.title]

    @staticmethod
    def import_record(values):
        c = Chapter.objects.get_or_create(book=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()
        return c

    def __str__(self):
        return f'{ self.book.title} - {self.order} - {self.title}'