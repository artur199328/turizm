# Generated by Django 4.0.5 on 2022-06-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aboutpage_delete_homepage2'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='about2',
            field=models.TextField(null=True, verbose_name='Aboutpage about2'),
        ),
    ]