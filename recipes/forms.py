from django import forms

from .models import Comment, Recipe, Chef

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('nick', 'c_title', 'text')

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('r_title', 'ingredients', 'process')

class ChefForm(forms.ModelForm):

    class Meta:
        model = Chef
        fields = ('name', 'age', 'experience')