from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView

# Create your views here.








def home(request, category_slug=None):
    blog_post = BlogPost.objects.all()
    featured_recipe = FeaturedRecipe.objects.all()
    recipes = Recipe.objects.all()[::-1]

    if category_slug:
        # Filter recipes based on the provided category_slug
        recipes = recipes.filter(category=category_slug)

    # Assuming you have a list of categories available in your model
    categories = Recipe.CATEGORY_CHOICES

    context = {
        'articles': blog_post,
        'featureds': featured_recipe,
        'recipes': recipes,
        'categories': categories,  # Include the categories in the context
        'category': category_slug,
    }
    return render(request, 'ketosite/home.html', context)






def blog(request):
    article = BlogPost.objects.all()
    categories = Recipe.CATEGORY_CHOICES


    context = {
        'articles': article,
         'categories': categories,
    }
    return render(request, 'ketosite/blog.html', context)





class BlogPostDetailView(DetailView):
    model = BlogPost
    template = 'ketosite/blogpost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = BlogPost.objects.all()
        
        # Add the categories to the context
        context['categories'] = Recipe.CATEGORY_CHOICES
        context['articles'] = articles
        

        return context





def featured(request):
    return render(request, 'ketosite/blog.html')




class FeaturedPost(DetailView):
    model = FeaturedRecipe
    template = 'ketosite/featuredpost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_post = BlogPost.objects.all()
        
        # Add the categories to the context
        context['categories'] = Recipe.CATEGORY_CHOICES
        context['articles'] = blog_post

        return context




def all_recipes(request, category_slug=None):
    recipes = Recipe.objects.all()[::-1]
    categories = Recipe.CATEGORY_CHOICES
    articles = BlogPost.objects.all()

    if category_slug and category_slug != 'all-recipes':
        # Filter recipes based on the provided category_slug
         recipes = Recipe.objects.filter(category=category_slug)[::-1]

    context = {
        'recipes': recipes,
        'categories': categories,
        'selected_category': category_slug, 
        'articles':articles,
    }
    return render(request, 'ketosite/all_recipes.html', context)




class RecipePost(DetailView):
    model = Recipe
    template= 'ketosite/recipespost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_post = BlogPost.objects.all()
        
        # Add the categories to the context
        context['categories'] = Recipe.CATEGORY_CHOICES
        context['articles'] = blog_post

        return context






def recipe_list(request, category_slug=None):
    recipes = Recipe.objects.all()[::-1]

    if category_slug:
        # Filter recipes based on the provided category_slug
        recipes = recipes.filter(category=category_slug)

    context = {
        'recipes': recipes,
        'category': category_slug
    }

    return render(request, 'ketosite/recipe_list.html', context)




def products(request):
    return render(request, 'ketosite/products.html')






def about(request):
    categories = Recipe.CATEGORY_CHOICES
    blog_post = BlogPost.objects.all()

    context = {
        'categories': categories,
        'articles': blog_post
    }
    return render(request, 'ketosite/about-us.html', context)






def contact(request):
    categories = Recipe.CATEGORY_CHOICES
    blog_post = BlogPost.objects.all()

    context = {
        'categories': categories,
        'articles': blog_post
    }
    return render(request, 'ketosite/contact-us.html', context)





def disclaimer(request):
    categories = Recipe.CATEGORY_CHOICES
    blog_post = BlogPost.objects.all()

    context = {
        'categories': categories,
        'articles': blog_post
    }
    return render(request, 'ketosite/disclaimer.html', context)