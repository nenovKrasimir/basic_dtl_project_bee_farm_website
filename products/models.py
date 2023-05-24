from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.FloatField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(500)])
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
