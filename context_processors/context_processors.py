from blog.models import Article , Category




def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')[:2]
    return {'recent_articles': recent_articles}




def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}