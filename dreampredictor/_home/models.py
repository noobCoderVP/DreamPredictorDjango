from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    age = models.IntegerField(validators=[
                              MaxValueValidator(100), MinValueValidator(12)])
