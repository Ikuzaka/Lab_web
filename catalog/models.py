from django.db import models
from login.models import MyUser

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True)
    about = models.TextField()
    cost=models.CharField(max_length=50)
    favorite_by = models.ManyToManyField(MyUser, blank=True)

    @property
    def favorites(self):
        return self.favorite_by.count()

