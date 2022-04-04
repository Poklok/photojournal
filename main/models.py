from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/posts', default=True)
    title = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
