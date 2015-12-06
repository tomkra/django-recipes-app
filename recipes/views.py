from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe, Chef
from .forms import CommentForm, RecipeForm, ChefForm
from django.utils import timezone


# Create your views here.

def index(request):
    latest_recipe_list = Recipe.objects.order_by('-date_published')[:5]
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'recipes/index.html', context)

def recipes_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipes_detail.html', {'recipe': recipe})

def chefs_detail(request, chef_id):
    chef = get_object_or_404(Chef, pk=chef_id)
    return render(request, 'recipes/chefs_detail.html', {'chef' : chef})

def all_recipes(request):
    list_of_recipes = Recipe.objects.order_by('-date_published')
    context = {'list_of_recipes': list_of_recipes}
    return render(request, 'recipes/all_recipes.html', context)

def all_chefs(request):
    list_of_chefs = Chef.objects.order_by('name')
    context = {'list_of_chefs': list_of_chefs}
    return render(request, 'recipes/all_chefs.html', context)

def add_comment(request, recipe_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = Recipe.objects.get(id=recipe_id)
            comment.date_commented = timezone.now()
            comment.save()
            return redirect('recipes_detail', recipe_id)
        else:
            return redirect('add_comment', recipe_id)
    else:
        form = CommentForm()
        recipeid = recipe_id
    return render(request, 'recipes/add_comment.html', {'form' : form, 'recipeid' : recipeid})

def add_recipe(request, chef_id):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.chef = Chef.objects.get(id=chef_id)
            recipe.date_published = timezone.now()
            recipe.save()
            return redirect('recipes_detail', recipe.id)
        else:
            return redirect('add_recipe', chef_id)
    else:
        form = CommentForm()
        chefid = chef_id
    return render(request, 'recipes/add_recipe.html', {'form' : form, 'chefid' : chefid})

def form_error(request):
    return render(request, 'recipes/form_error.html')

def add_chef(request):
    if request.method == "POST":
        form = ChefForm(request.POST)
        if form.is_valid():
            chef = form.save(commit=False)
            chef.date_added = timezone.now()
            chef.save()
            return redirect('chefs_detail', chef.id)
        else:
            return redirect('add_chef')
    else:
        form = ChefForm()
    return render(request, 'recipes/add_chef.html', {'form' : form})