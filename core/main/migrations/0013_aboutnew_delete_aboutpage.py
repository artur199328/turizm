# Generated by Django 4.0.5 on 2022-06-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_aboutpage_delete_aboutpag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Aboutnew name')),
                ('about', models.TextField(verbose_name='Aboutnew about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Aboutnew logo img')),
            ],
            options={
                'verbose_name': 'Aboutnew',
                'verbose_name_plural': 'Aboutnews',
            },
        ),
        migrations.DeleteModel(
            name='Aboutpage',
        ),
    ]
