from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify



class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title





class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category , related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True , blank=True)






    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article , self).save()

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return f'{self.title} - {self.body[:30]}'



    class Meta:
        ordering = ('-created',)





class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self',null=True,blank=True ,related_name='replies', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        return f'{self.user} - {self.article} - {self.created_at}'







class Massage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True , null=True)


    def __str__(self):
        return self.title












