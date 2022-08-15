from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

# Главная страница
def index(request): 
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

# Страница с постами, отфильтрованными по группам;
# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Посты по группам {slug}') 

def group_list(request):
    template = 'posts/group_list.html' 
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {'title': title,}    
    return render(request, template, context)