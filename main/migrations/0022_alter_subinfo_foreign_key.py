# Generated by Django 4.0.3 on 2022-03-14 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_subinfo_foreign_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subinfo',
            name='foreign_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.info', verbose_name='Тема'),
        ),
    ]
