# Generated by Django 5.0.6 on 2025-02-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('description', models.TextField(null=True, verbose_name='Product Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image 3')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
