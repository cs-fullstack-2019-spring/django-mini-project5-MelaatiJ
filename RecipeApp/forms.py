from django import forms
from .models import UserModel, RecipeModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude =["User_fk"]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude = ["recipe_fk"]
