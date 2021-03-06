# Generated by Django 3.1.7 on 2021-09-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocapp', '0005_delete_merchandise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(default=0)),
                ('availability', models.CharField(blank=True, choices=[('Stock', 'In Stock'), ('Out', 'Out Of Stock'), ('Pre', 'Pre-Order')], default='Stock', max_length=30, null=True)),
                ('product_condition', models.CharField(blank=True, choices=[('Brand New', 'Brand New'), ('Refurbished', 'Refurbished')], default='Brand New', max_length=30, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('is_slider', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('brand', models.CharField(blank=True, default='Home&Craft', max_length=20, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
