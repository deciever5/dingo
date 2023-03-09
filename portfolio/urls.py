from django.urls import path
from .views import main, me, contact

urlpatterns = [
    path('', main, name='main'),
    path('me', me, name='me'),
    path('contact', contact, name='contact'),

]
