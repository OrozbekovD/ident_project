from django.db import models
from phonenumber_field.modelfields import PhoneNumberField




class Slider(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='media/slider', verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Banner(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='media/banner', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class BannerSlider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='media/bannersslider', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/news', verbose_name='Фото', default='')

    def __str__(self):
        return self.title

class Service(models.Model):
    pass

class ProductInner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/productinner', verbose_name='Фото')

    def __str__(self):
        return self.title


class About(models.Model):
    pass

CONTACTS_CHOICES = [
        ('DC', 'Диллерские центры'),
        ('SC', 'Cервисные центры'),
    ]

class Contact(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес', default='')
    number = PhoneNumberField(unique=True, region='KG', verbose_name='Номер')
    email = models.EmailField(max_length=255, verbose_name='Почта', default='')
    choices = models.CharField(max_length=255, choices=CONTACTS_CHOICES)
    def __str__(self):
        return self.title

class Email(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(max_length=255, verbose_name='Почта')

    def __str__(self):
        return self.title

class Phones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    number = PhoneNumberField(unique=True, region='KG', verbose_name='Номер')

    def __str__(self):
        return self.title
class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    places = models.CharField(max_length=255, verbose_name='Место')

    def __str__(self):
        return self.title
