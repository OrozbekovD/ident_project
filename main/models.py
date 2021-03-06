from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from embed_video.fields import EmbedVideoField
from main.validators import validate_file_extension


class Catalog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(to='Hashtag')
    catalog = models.ForeignKey(to=Catalog, on_delete=models.CASCADE, verbose_name='Catalog', null=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', default='')
    image = models.ImageField(upload_to='productimage', verbose_name='Фото продукции', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Название продукции')

    def __str__(self):
        return self.title


class ProductWall(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(verbose_name='Баннер продукции', upload_to='productwall')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=255, verbose_name='Hashtag')

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='slider', verbose_name='Фото')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='banner', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

    def __str__(self):
        return self.title


class BannerSlider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='bannersslider', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

    def __str__(self):
        return self.title


class New(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='news', verbose_name='Фото', default='')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')

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
    info = models.ForeignKey(to=Info, on_delete=models.CASCADE, verbose_name='Тема', default='')

    def __str__(self):
        return self.title


class ServiceIntro(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='serviceintro')

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', default='')
    description = models.TextField(verbose_name='Описание', default='')

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='serviceimage', default='', null=True, blank=True)


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', default='')
    description = models.TextField(verbose_name='Описание', default='')
    url = EmbedVideoField(verbose_name='Video', default='')

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


class Phone(models.Model):
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
