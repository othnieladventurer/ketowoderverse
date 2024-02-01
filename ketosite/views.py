from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView

from django.views.decorators.cache import cache_page

# Create your views here.











@cache_page( 60 * 60)
def home(request, category_slug=None):
    blog_post = BlogPost.objects.all()
    featured_recipe = FeaturedRecipe.objects.all()
    recipes = Recipe.objects.all()


    page_title = 'Ketowonderverse'
    meta_description = 'Explore keto diet facts on our home page—dive into a universe of tips, recipes, and resources for weight loss and improved health. Discover keto wonders! '
    page_image = 'static/images/carousel.webp'

    if category_slug:
        # Filter recipes based on the provided category_slug
        recipes = recipes.filter(category=category_slug)

    # Assuming you have a list of categories available in your model
    categories = Recipe.CATEGORY_CHOICES

    context = {
        'articles': blog_post,
        'featureds': featured_recipe,
        'recipes': recipes,
        'categories': categories,  
        'category': category_slug,
        'page_title': page_title,
        'meta_description': meta_description,
        'page_image': page_image,
    }
    return render(request, 'ketosite/home.html', context)





@cache_page( 60 * 60)
def blog(request):
    article = BlogPost.objects.all()
    categories = Recipe.CATEGORY_CHOICES

    page_title = 'Blog Posts Ketowonderverse'
    meta_description = 'Explore inspiration on our Blogs page, where trends, heartwarming stories, and expert gift ideas unfold. Let our blogs guide you for memorable celebrations.'
    page_image = 'static/images/carousel.webp'




    context = {
        'articles': article,
        'categories': categories,
        'page_title': page_title,
        'meta_description': meta_description,
        'page_image': page_image,
    }
    return render(request, 'ketosite/blog.html', context)





class BlogPostDetailView(DetailView):
    model = BlogPost
    template = 'ketosite/blogpost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = BlogPost.objects.all()
        related_articles = self.object.related_articles.all()
        
        # Add the categories to the context
        context['categories'] = Recipe.CATEGORY_CHOICES
        context['articles'] = articles
        context['related_articles'] = related_articles
        

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



@cache_page( 60 * 60)
def all_recipes(request, category_slug=None):
    recipes = Recipe.objects.all()[::-1]
    categories = Recipe.CATEGORY_CHOICES
    articles = BlogPost.objects.all()

    page_title = 'All recipes Ketowonderverse'
    meta_description = 'Unlock a world of flavor with KetoWonderverses keto recipes. From savory to sweet, find low-carb culinary delights to enhance your keto meal experience.'
    page_image = 'static/images/carousel.webp'

    if category_slug and category_slug != 'all-recipes':
        # Filter recipes based on the provided category_slug
         recipes = Recipe.objects.filter(category=category_slug)[::-1]

    context = {
        'recipes': recipes,
        'categories': categories,
        'selected_category': category_slug, 
        'articles':articles,
        'page_title': page_title,
        'meta_description': meta_description,
        'page_image': page_image,
    }
    return render(request, 'ketosite/all_recipes.html', context)




class RecipePost(DetailView):
    model = Recipe
    template= 'ketosite/recipespost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_post = BlogPost.objects.all()
        related_recipes= self.object.related_recipes.all()
        
        # Add the categories to the context
        context['categories'] = Recipe.CATEGORY_CHOICES
        context['articles'] = blog_post
        context['related_recipes'] = related_recipes

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

    page_title = 'About Ketowronderverse'
    meta_description = 'Discover the heart behind KetoWonderverse. Learn about our mission to guide and inspire you on your keto and weight loss journey'
    page_image = 'static/images/carousel.webp'

    context = {
        'categories': categories,
        'articles': blog_post,
        'page_title': page_title,
        'meta_description': meta_description,
        'page_image': page_image,
        
    }
    return render(request, 'ketosite/about-us.html', context)






def contact(request):
    categories = Recipe.CATEGORY_CHOICES
    blog_post = BlogPost.objects.all()

    page_title = 'Contact Ketowronderverse'
    meta_description = 'Reach out to KetoWonderverse for inquiries, collaborations, or simply to share your keto and low-carb experiences. We are here to support you!'
    page_image = 'static/images/carousel.webp'

    context = {
        'categories': categories,
        'articles': blog_post,
        'page_title': page_title,
        'meta_description': meta_description,
        'page_image': page_image,
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