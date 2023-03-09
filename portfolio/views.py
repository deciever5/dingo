# Create your views here.
from django.shortcuts import render


# Create your views here.

def main(request):
    c = {"title": "dodawanie"}
    return render(
        request=request,
        template_name="portfolio\\main.html",
        context=c
    )


def me(request):
    c = {"title": "dodawanie"}
    return render(
        request=request,
        template_name="portfolio\\aboutme.html",
        context=c
    )


def contact(request):
    c = {"title": "dodawanie"}
    return render(
        request=request,
        template_name="portfolio\\contact.html",
        context=c
    )
