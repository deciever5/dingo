# Create your views here.
from django.http import HttpResponse


# Create your views here.
def greetings(request):
    return HttpResponse("Hello World!")


def call(request, name):
    return HttpResponse(f'Hello {name}')
