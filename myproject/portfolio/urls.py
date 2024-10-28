from django.urls import path
from .views import index,skills,portfolio,books,Posts

urlpatterns = [
    path('',books,name='books'),
    path('Posts',Posts,name='Posts'),
    path('about_me',index,name='about_me'),
    path('skills',skills,name='skills'),
    path('portfolio',portfolio,name='portfolio'),
]
