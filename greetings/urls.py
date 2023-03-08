from django.urls import path
from .views import greetings, call

urlpatterns = [
    path('', greetings),
    path('<name>', call),
]
