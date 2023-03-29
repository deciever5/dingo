# Create your views here.
from django.shortcuts import render


# Create your views here.

def main(request):
    dingo_image_url = 'https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/dingo-portrait-levana-sietses.jpg'
    context = {'dingo_image_url': dingo_image_url}
    return render(
        request=request,
        template_name="portfolio/main.html",
        context=context
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
