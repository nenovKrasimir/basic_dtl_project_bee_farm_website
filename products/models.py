from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.FloatField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(500)])
    image = models.ImageField(upload_to='images/')