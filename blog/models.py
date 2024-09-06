from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html


class Category(models.Model):
    title = models.CharField(max_length=50 , verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'





class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name='نویسنده ی مقالات')
    category = models.ManyToManyField(Category , related_name='articles', verbose_name='دسته بندی')
    title = models.CharField(max_length=100 , verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to="images/articles" , verbose_name='عکس' , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True , blank=True)






    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article , self).save()

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})



    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')



    def __str__(self):
        return f'{self.title} - {self.body[:30]}'



    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'




class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self',null=True,blank=True ,related_name='replies', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        return f'{self.user} - {self.article} - {self.created_at}'


    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'



class Massage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True , null=True)


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'




class Like(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='likes' , verbose_name='کاربر')
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='likes' , verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.user.username} - {self.article.title}'



    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created_at',)




