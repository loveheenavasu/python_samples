from django.contrib import admin

from .models import UserUniqueToken,Product

# Register your models here.
admin.site.register(UserUniqueToken)
admin.site.register(Product)