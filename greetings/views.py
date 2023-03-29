
from django.shortcuts import render

def welcome(request):
    return render(request, 'greetings/welcome.html')

def about(request):
    return render(request, 'greetings/about.html')

def contact(request):
    return render(request, 'greetings/contact.html')
