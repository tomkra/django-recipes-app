from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import datetime


# Create your models here.
class Chef(models.Model):
    Beginner  = 'Beginner'
    Advanced = 'Advanced'
    Expert = 'Expert'
    Magical = 'Magical'
    EXPERIENCES = (
        (Beginner, 'Beginner'),
        (Advanced, 'Advanced'),
        (Expert, 'Expert'),
        (Magical, 'Magical'), 
        )
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(110)])
    experience = models.CharField(max_length=50, choices=EXPERIENCES, default=Beginner)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.name + ": " + str(self.age) + ", " + self.experience

class Recipe(models.Model):
    chef = models.ForeignKey(Chef)
    r_title = models.CharField(max_length=70)
    ingredients = models.TextField(max_length=2000)
    process = models.TextField()
    date_published = models.DateTimeField()

    def __str__(self):
        return self.r_title + ", published: " + str(self.date_published.strftime("%H:%M:%S %d.%m.%Y"))

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe)
    nick = models.CharField(max_length=10)
    c_title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)
    date_commented = models.DateTimeField()

    def __str__(self):
        return self.nick + ": " + self.c_title + ", published: " + str(self.date_commented.strftime("%H:%M:%S %d.%m.%Y"))

    def was_commented_recently(self):
        return self.date_commented >= timezone.now() - datetime.timedelta(days=1)

#from recipes.models import Chef, Recipe, Comment