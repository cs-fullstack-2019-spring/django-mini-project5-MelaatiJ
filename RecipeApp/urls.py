from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newUser/", views.newUser, name="newUser"),
    path("allRecipes/", views.allRecipes, name="allRecipes"),
    path("newRecipe/", views.newRecipe, name="newRecipe"),
    path("editRecipe/<int:id>/", views.editRecipe, name="editRecipe"),
    path("deleteRecipe/<int:id>/", views.deleteRecipe, name="deleteRecipe"),
    path("recipeDescription/", views.recipeDescription, name="recipeDescription"),
]
