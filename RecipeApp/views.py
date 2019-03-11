from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserModel, UserForm, RecipeModel, RecipeForm
from django.contrib.auth.models import User


# Create your views here.
# function to make a new user
def newUser(request):
    #fo
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        # creates new user
        User.objects.create_user(request.POST["name"], "", request.POST["password"])
        # save form
        form.save()
        return redirect('home')
        #making it into context
    context = {
        'form': form
    }
    return render(request, 'RecipeApp/newUser.html', context)


def home(request):
    # if the user is logged in
    if request.user.is_authenticated:
        # get it by the user
        currentChef = UserModel.objects.get(name=request.user)
        myRecipes = RecipeModel.objects.filter(chef=currentChef)
    else:
        # passing it through
        myRecipes = ""
    context = {
        "myRecipes": myRecipes
    }
    return render(request, "RecipeApp/index.html", context)


def allRecipes(request):
    return render(request, "RecipeApp/allRecipes.html")


def newRecipe(request):
    form = RecipeForm(request.POST or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        currentChef = UserModel.objects.get(name=request.user)
        RecipeModel.objects.create(image=request.POST['image'], nameOfMeal=request.POST["nameOfMeal"],
                                   shortDescription=request.POST["shortDescription"],
                                   dateCreated=request.POST['dateCreated'],chef=request.POST['chef'],ingredients=request.POST["ingredients"], directions=['directions'])
        return redirect("home")
    return render(request, "RecipeApp/newRecipe.html", context)


def editRecipe(request):
    return HttpResponse("not yet")


def deleteRecipe(request):
    return HttpResponse("delete recipe")


def recipeDescription(request):
    return render(request, "RecipeApp/recipeDescription.html")
