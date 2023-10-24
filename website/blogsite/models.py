
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    url = models.URLField(default="10.1093/ajae/aaq063")
    
    def _str_(self):
        return self.title + ' ' + str(self.author)
    def get_absolute_url(self):
        return reverse('post')
    


