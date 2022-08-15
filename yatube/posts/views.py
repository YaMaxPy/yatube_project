from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request): 
    template = 'posts/index.html' 
    title = 'Это главная страница проекта Yatube'
    context = {'title': title,}  
    return render(request, template, context)

# Страница с постами, отфильтрованными по группам;
# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Посты по группам {slug}') 

def group_list(request):
    template = 'posts/group_list.html' 
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {'title': title,}    
    return render(request, template, context)