from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Category

def posts_by_category(request, category_id):
    #Fetching the posts that belongs to category with the category_ID
    posts = Blog.objects.filter(status='Published', category=category_id)
    
    #try:
    #    category = Category.objects.get(pk=category_id)
    #except:
    #    return redirect('home')
    
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)