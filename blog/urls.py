from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>'  , views.ArticleDetailView.as_view() , name='article_detail'),
    path('list' , views.articles_list , name='articles_list'),
    path('category/<int:pk>',views.category_detail,  name='category_detail'),
    path('search/' , views.search , name='search_articles'),
    path('contactus' , views.contactus, name='contactus'),
    path('users' , views.UserList.as_view() , name='users_list'),
    path('like/<slug:slug>/<int:pk>' , views.like, name='like'),
]