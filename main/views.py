
from django.shortcuts import render

from main.models import Slider, Contact, Banner, BannerSlider, News, ProductInner, Info, SubInfo, LastBanner


def index(request):
    sliders = Slider.objects.all()
    banner = Banner.objects.first()
    bannersl = BannerSlider.objects.all()
    news = News.objects.all()
    info = Info.objects.first()
    subinfo = SubInfo.objects.filter(foreign_key=info)[:3]
    lastbanner = LastBanner.objects.all()[:3]

    context = {'sliders': sliders, 'banner': banner, 'bannersl': bannersl,
                            'news': news, 'info': info, 'subinfo': subinfo, 'lastbanner': lastbanner}

    return render(request, 'pages/index.html', context)

def about(request):


    return render(request, 'pages/about.html', locals())

def service(request):
    return render(request, 'pages/service.html', locals())

def contact(request):
    contacts = Contact.objects.all()

    return render(request, 'pages/contacts.html', locals())

def catalog(request):

    return render(request, 'pages/catalog.html', locals())

def product_inner(request):
    product_iner = ProductInner.objects.all()

    return render(request, 'pages/product-inner.html', locals())

def news_detail(request):
    news = News.objects.all()
    return render(request, 'pages/news_detail.html', locals())
