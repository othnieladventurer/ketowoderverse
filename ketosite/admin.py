from django.contrib import admin
from .models import *



# Register your models here.
admin.site.register(BlogPost)
admin.site.register(FeaturedRecipe)
admin.site.register(Product)
admin.site.register(Recipe)