# Create your views here.
from django.shortcuts import render


# Create your views here.

def main(request):
    return render(
        request=request,
        template_name="portfolio/main.html",
    )


def me(request):
    return render(
        request=request,
        template_name="portfolio/aboutme.html",
    )


def contact(request):
    return render(
        request=request,
        template_name="portfolio/contact.html",
    )
