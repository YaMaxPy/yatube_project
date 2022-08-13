from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request): 
    template = 'posts/index.html'   
    return render(request, template)

# Страница с постами, отфильтрованными по группам;
# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Посты по группам {slug}') 

def group_list(request):
    template = 'posts/group_list.html'   
    return render(request, template)