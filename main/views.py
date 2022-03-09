
from django.shortcuts import render

from main.models import Products, Slider, Contact, Banner


def index(request):
    sliders = Slider.objects.all()
    banner = Banner.objects.get()
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', locals())

def catalog(request):
    return render(request, 'catalog.html')

def product_inner(request):
    return render(request, 'product-inner.html')

def news(request):
    return render(request, 'index.html')
