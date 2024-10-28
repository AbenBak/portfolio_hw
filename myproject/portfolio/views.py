from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Post
def index(request):
    return render(request,'about_me.html')
def skills(request):
    return render(request,'skills.html')
def portfolio(request):
    return render(request,'portfolio.html')
def books(request):
    books=Book.objects.all()
    context={
        "books":books
    }
    return render(request,'book.html',context)
def Posts(request):
    Posts=Post.objects.all()
    context={
        "Posts":Posts
    }
    return render(request,'book.html',context)