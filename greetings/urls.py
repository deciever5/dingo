from django.urls import path
from greetings.views import  welcome

urlpatterns = [
   path('', welcome, name="welcome"),

]