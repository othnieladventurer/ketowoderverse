from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField





# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_post_images/')
    image_alt = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    related_articles = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title
    

    
    def get_absolute_url(self):
        return reverse("ketosite:blog-post", kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





class FeaturedRecipe(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='featured_recipe_images/')
    image_alt = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    related_articles = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("ketosite:featured_post", kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('all recipes', 'All Recipes'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
    ]

    title = models.CharField(max_length=255)
    content = RichTextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='recipe_images/')
    image_alt = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    related_recipes = models.ManyToManyField('self', blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True)

    def __str__(self):
        return self.title
    


    def get_absolute_url(self):
        return reverse("ketosite:recipe_post", kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
    def get_queryset(self):
        return super().get_queryset().order_by('-date')
    


    






class Product(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/')
    image_alt = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    keto_friendly = models.BooleanField(default=True)
    ingredients = models.TextField(help_text='List of ingredients, comma-separated')

    def __str__(self):
        return self.name

