from django.shortcuts import render
from .models import Page

# Create your views here.
def page(request, slug):
    page= Page.objects.get(slug=slug)#Campo de la base y después el parámetro de la url
    return render(request, "pages/page.html", {
        "title":page.title,
        "page":page
    })