
from django.shortcuts import render

from main.models import Slider, Contact, Banner, BannerSlider, News, ProductInner, Info, SubInfo, LastBanner, \
    ContactWall, Service, About


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

    abouts = About.objects.first()

    context = {'abouts': abouts}
    return render(request, 'pages/about.html', context)

def service(request):
    service = Service.objects.first()
    contacts = Contact.objects.all()

    context = {'service': service, 'contacts': contacts}
    return render(request, 'pages/service.html', context)

def contact(request):
    contacts = Contact.objects.all()
    wall = ContactWall.objects.first()

    context = {'contacts': contacts, 'wall': wall}

    return render(request, 'pages/contacts.html', context)

def catalog(request):

    return render(request, 'pages/catalog.html', locals())

def product_inner(request):
    product_iner = ProductInner.objects.all()

    return render(request, 'pages/product-inner.html', locals())

def news_detail(request, pk):
    new = News.objects.get(pk=pk)
    context = {'new': new}
    return render(request, 'pages/news_detail.html', context)
