from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница с постами, отфильтрованными по группам;
# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Посты по группам {slug}') 