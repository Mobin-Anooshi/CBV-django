from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
