from django.shortcuts import render
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.order_by('-created')[:2]
    return render(request, 'home/index.html', {'articles': articles , 'recent_articles': recent_articles})