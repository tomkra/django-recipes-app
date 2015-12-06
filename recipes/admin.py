from django.contrib import admin

from .models import Chef, Recipe, Comment

class ChefAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Person Information', {'fields': ['name', 'experience', 'age']}),
        ('Date information', {'fields': ['date_added']}),
    ]

    list_display = ('name', 'age', 'experience')

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Recipe Information', {'fields': ['chef', 'r_title', 'ingredients', 'process']}),
        ('Date information', {'fields': ['date_published']}),
    ]

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Comment', {'fields': ['recipe', 'c_title', 'nick', 'text']}),
        ('Date', {'fields': ['date_commented']}),
    ]

admin.site.register(Chef, ChefAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
