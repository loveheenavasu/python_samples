from django.contrib import admin
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('',views.createuser,name="createuser"),
    path('login',views.login,name="login"),
    path('profile',views.profile,name="profile"),
    path("logout",views.logout,name="logout"),
  
    
  

]
