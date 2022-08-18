
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserUniqueToken(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)

class Product(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    number_of_products=models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.number_of_products}'