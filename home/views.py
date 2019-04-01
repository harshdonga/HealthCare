from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def appointment(request):
    return render(request, 'home/appointment.html')


def contact(request):
    return render(request, 'home/contact.html')


def gallery(request):
    return render(request, 'home/gallery.html')


















