# Generated by Django 4.0.3 on 2022-03-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default='', max_length=150, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bannerslider',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='email',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lastbanner',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='phones',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='place',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='choices',
            field=models.CharField(choices=[('DC', 'Дилерские центры'), ('SC', 'Cервисные центры')], max_length=255),
        ),
    ]
