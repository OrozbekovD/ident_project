from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from main.models import Slider, Contact, Banner, BannerSlider, New, Info, SubInfo, LastBanner, \
    ContactWall, Service, About, ServiceIntro, ServiceImage, Product, Catalog, Hashtag, ProductWall
from django.db.models import Q

def index(request):
    sliders = Slider.objects.all()
    banner = Banner.objects.first()
    bannersl = BannerSlider.objects.all()
    news = New.objects.filter(is_active=True)[:4]
    info = Info.objects.first()
    subinfo = SubInfo.objects.filter(info=info)[:3]
    lastbanner = LastBanner.objects.all()[:3]

    context = {'sliders': sliders, 'banner': banner, 'bannersl': bannersl,
               'news': news, 'info': info, 'subinfo': subinfo, 'lastbanner': lastbanner}

    return render(request, 'pages/index.html', context)


def about(request):
    abouts = About.objects.first()
    contacts = Contact.objects.all()

    context = {'abouts': abouts, 'contacts': contacts}
    return render(request, 'pages/about.html', context)


def service(request):
    service = Service.objects.all()
    contacts = Contact.objects.all()
    service_intro = ServiceIntro.objects.first()
    service_image = ServiceImage.objects.first()
    context = {'service': service, 'contacts': contacts, 'service_intro': service_intro, 'service_image': service_image}
    return render(request, 'pages/service.html', context)


def contact(request):
    contacts = Contact.objects.all()
    wall = ContactWall.objects.first()

    context = {'contacts': contacts, 'wall': wall}

    return render(request, 'pages/contacts.html', context)


def catalog(request, pk):
    hashtags = Hashtag.objects.all()
    try:
        catalogs = Catalog.objects.get(pk=pk)
    except ObjectDoesNotExist:
        catalogs = get_object_or_404
        return catalogs

    products = Product.objects.filter(catalog=catalogs)
    wall = ProductWall.objects.filter(is_active=True)

    context = {'catalogs': catalogs, 'products': products, 'hashtags': hashtags, 'wall': wall}

    return render(request, 'pages/catalog.html', context)


def product_inner(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        product = get_object_or_404
        return product

    catalogs = Catalog.objects.get(product=pk)

    context = {'product': product, 'catalogs': catalogs}

    return render(request, 'pages/product-inner.html', context)


def news_page(request):

    search_query = request.GET.get('search', '')

    if search_query:
        news_list = New.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    else:
        news_list = New.objects.filter(is_active=True)

    paginator = Paginator(news_list, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page{}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {'news_list': page, 'is_paginated': is_paginated, 'prev_url': prev_url, 'next_url': next_url}
    return render(request, 'pages/news.html', context)


def new_detail(request, pk):
    try:
        new = New.objects.get(pk=pk)
    except ObjectDoesNotExist:
        new = get_object_or_404
        return new
    context = {'new': new}
    return render(request, 'pages/news_detail.html', context)
