from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Products(models.Model):
    pass

class Slider(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Banner(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Service(models.Model):
    pass


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