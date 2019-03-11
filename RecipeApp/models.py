from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField()
    profilePic = models.CharField(max_length=800, default="")
    password= models.CharField(max_length=100, default="")
    User_fk = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    image = models.CharField(max_length=900, default="")
    nameOfMeal = models.CharField(max_length=200, default="")
    shortDescription = models.TextField(max_length=200, default="")
    dateCreated = models.DateField(default=date.today)
    chef = models.CharField(max_length=100, default="")
    ingredients = models.TextField(max_length=800, default="")
    directions = models.TextField(max_length=900, default="")
    recipe_fk = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nameOfMeal
