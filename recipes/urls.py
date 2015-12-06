from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipe/(?P<recipe_id>[0-9]+)/$', views.recipes_detail, name='recipes_detail'),
    url(r'^chef/(?P<chef_id>[0-9]+)/$', views.chefs_detail, name='chefs_detail'),
    url(r'^recipes/$', views.all_recipes, name='all_recipes'),
    url(r'^chefs/$', views.all_chefs, name='all_chefs'),
    url(r'^addcomment/(?P<recipe_id>[0-9]+)/', views.add_comment, name='add_comment'),
    url(r'^addrecipe/(?P<chef_id>[0-9]+)/', views.add_recipe, name='add_recipe'),
    url(r'^addchef/$', views.add_chef, name='add_chef'),
    url(r'^form_error/', views.form_error, name='form_error'),
]