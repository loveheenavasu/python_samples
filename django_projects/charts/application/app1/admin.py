from django.contrib import admin
from .models import UserUniqueToken,Product
from admin_list_charts.admin import ListChartMixin
# Register your models here.
admin.site.register(UserUniqueToken)
admin.site.register(Product)