# Generated by Django 4.0.5 on 2022-06-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_hotelpage2'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelpage2',
            name='name2',
            field=models.CharField(max_length=100, null=True, verbose_name='Hotelpage2 name2'),
        ),
        migrations.AddField(
            model_name='hotelpage2',
            name='name3',
            field=models.CharField(max_length=100, null=True, verbose_name='Hotelpage2 name3'),
        ),
        migrations.AddField(
            model_name='hotelpage2',
            name='name4',
            field=models.CharField(max_length=100, null=True, verbose_name='Hotelpage2 name4'),
        ),
        migrations.AddField(
            model_name='hotelpage2',
            name='name5',
            field=models.CharField(max_length=100, null=True, verbose_name='Hotelpage2 name5'),
        ),
        migrations.AddField(
            model_name='hotelpage2',
            name='name6',
            field=models.CharField(max_length=100, null=True, verbose_name='Hotelpage2 name6'),
        ),
    ]