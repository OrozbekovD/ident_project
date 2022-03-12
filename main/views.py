
from django.shortcuts import render

from main.models import Slider, Contact, Banner, BannerSlider, News, ProductInner


def index(request):
    sliders = Slider.objects.all()
    banner = Banner.objects.first()
    bannersl = BannerSlider.objects.all()
    news = News.objects.all()

    context = {'sliders': sliders, 'banner': banner, 'bannersl': bannersl, 'news': news }

    return render(request, 'index.html', context )

def about(request):


    return render(request, 'about.html', locals())

def service(request):
    return render(request, 'service.html', locals())

def contact(request):
    contacts = Contact.objects.all()

    return render(request, 'contacts.html', locals())

def catalog(request):

    return render(request, 'catalog.html', locals())

def product_inner(request):
    product_iner = ProductInner.objects.all()

    return render(request, 'product-inner.html', locals())

def news(request):
    return render(request, 'index.html')
