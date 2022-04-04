from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='profile/avatar', default=True)

    def __str__(self):
        return self.user.username
