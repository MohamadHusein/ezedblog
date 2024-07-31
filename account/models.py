from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/images' , blank=True , null=True)




    def __str__(self):
        return self.user.username


