# Generated by Django 4.0.5 on 2022-06-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_homepage2_alter_homepage_name2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='Aboutpage about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Aboutpage logo img')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.DeleteModel(
            name='Homepage2',
        ),
    ]
