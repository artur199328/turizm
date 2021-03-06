# Generated by Django 4.0.5 on 2022-06-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_homepage5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Homepage6 logo img')),
                ('name', models.CharField(max_length=100, verbose_name='Homepage6 name')),
                ('about', models.TextField(verbose_name='Homepage6 about')),
            ],
            options={
                'verbose_name': 'Homepage6',
                'verbose_name_plural': 'Homepages6',
            },
        ),
    ]
