from django.shortcuts import render , get_object_or_404 , redirect
from blog.models import Article, Category , Comment , Massage , Like
from django.core.paginator import Paginator
from .forms import ContactUsForm , MassageForm
from django.views.generic.base import View , TemplateView , RedirectView
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView
from django.http import JsonResponse




def article_detail(request , slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article , user=request.user , parent_id=parent_id)
    return render(request, 'blog/article_detail.html', {'article':article})






def articles_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request , 'blog/articles_list.html' , {'articles':objects_list})





def category_detail(request , pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request , 'blog/articles_list.html' , {'articles':articles})



def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request , 'blog/articles_list.html' , {'articles':objects_list})








def contactus(request):
    if request.method == 'POST':
        form = MassageForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MassageForm()
    return render(request , 'blog/contact_us.html', {'form':form})




class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(article__slug=self.object.slug , user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context





class ArticleList(ListView):
    queryset = Article.objects.all()
    template_name = 'blog/articles_list.html'




class UserList(ListView):
    queryset = User.objects.all()
    template_name = 'blog/user_list.html'






def like(request , slug , pk):
    try:
        like = Like.objects.get(article__slug=slug , user_id=request.user.id)
        like.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        Like.objects.create(article_id=pk , user_id=request.user.id)
        return JsonResponse({'response': 'liked'})









