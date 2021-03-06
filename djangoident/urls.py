"""djangoident URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import index, about, service, contact, catalog, product_inner, new_detail, news_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contacts/', contact, name='contacts'),
    path('catalog/<int:pk>', catalog, name='catalog'),
    path('product-inner/<int:pk>', product_inner, name='product_inner'),
    path('news/<int:pk>', new_detail, name='news_detail'),
    path('news/', news_page, name='news')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
