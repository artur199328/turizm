# Generated by Django 4.0.5 on 2022-06-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_hotelpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotelpage2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Hotelpage2 logo img')),
                ('price', models.IntegerField(verbose_name='Hotelpage2 price')),
                ('name', models.CharField(max_length=100, verbose_name='Hotelpage2 name')),
            ],
            options={
                'verbose_name': 'Hotelpage2',
                'verbose_name_plural': 'Hotelpages2',
            },
        ),
    ]