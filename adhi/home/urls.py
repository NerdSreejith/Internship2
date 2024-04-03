from django.urls import path,include
from . import views
urlpatterns = [
   
    path('',views.index,name="index"),
    path('regiter/',views.about,name="about"),
    path('login/',views.reg,name="reg")
]
