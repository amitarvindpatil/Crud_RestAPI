from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
