from django.shortcuts import render


def home(request):
    return render(request, "vitrine/home.html")


def about(request):
    return render(request, "vitrine/about.html")


def contact(request):
    return render(request, "vitrine/contact.html")
