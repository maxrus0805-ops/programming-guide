from django.shortcuts import render, get_object_or_404
from .models import ProgrammingLanguage

def index(request):
    """Главная страница со всеми языками"""
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'index.html', {'languages': languages})

def language_detail(request, slug):
    """Страница конкретного языка"""
    language = get_object_or_404(ProgrammingLanguage, slug=slug)
    return render(request, 'language_detail.html', {'language': language})

def popular_languages(request):
    """Страница популярных языков"""
    popular_langs = ProgrammingLanguage.objects.filter(is_popular=True)
    return render(request, 'popular.html', {'languages': popular_langs})