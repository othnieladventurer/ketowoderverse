from django.contrib import admin
from django.urls import path
from . import views

from .views import (BlogPostDetailView, FeaturedPost, RecipePost)


app_name = 'ketosite'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name="blog"),
    path('blog-post/<slug:slug>/', BlogPostDetailView.as_view(), name="blog-post"),

    path('featured/<slug:slug>/', FeaturedPost.as_view(), name="featured_post"),

    path('recipes/<slug:category_slug>/', views.all_recipes, name='all_recipes'),
    
    path('recipes/<slug:category_slug>/', views.recipe_list, name='recipe_list'),

    path('recipe/<slug:slug>/', RecipePost.as_view(), name="recipe_post"),
    


    path('products/', views.products, name="products"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('disclaimer/', views.disclaimer, name="disclaimer"),


]
