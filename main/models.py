from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from main.validators import validate_file_extension


class Slider(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='slider', verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Banner(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='banner', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class BannerSlider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='bannersslider', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='news', verbose_name='Фото', default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Info(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

class SubInfo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='subinfo')
    foreign_key = models.ForeignKey(to=Info, on_delete=models.CASCADE, verbose_name='Тема', default='')

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', default='')
    description = models.TextField(verbose_name='Описание', default='')
    image = models.ImageField(verbose_name='Фото', upload_to='serviceimage', default='', null='', blank=True)

    def __str__(self):
        return self.title


class ProductInner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='productinner', verbose_name='Фото')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', default='')
    description = models.TextField(verbose_name='Описание', default='')

    def __str__(self):
        return self.title

CONTACTS_CHOICES = [
        ('DC', 'Дилерские центры'),
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

class ContactWall(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='contactwall')



class Email(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(max_length=255, verbose_name='Почта')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Phones(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    number = PhoneNumberField(unique=True, region='KG', verbose_name='Номер')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    places = models.CharField(max_length=255, verbose_name='Место')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class LastBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null='', default='')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='lastbanner', verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Social(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    logo = models.FileField(verbose_name='Лого', validators=[validate_file_extension], blank=True, default='')
    url = models.URLField(verbose_name='Ссылка', blank=True)

    def __str__(self):
        return self.title

class Footer(models.Model):
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.description





