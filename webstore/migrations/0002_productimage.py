# Generated by Django 5.1.4 on 2024-12-29 10:04

import django.db.models.deletion
import webstore.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=webstore.models.ProductImage.product_image_upload_to)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='webstore.product')),
            ],
        ),
    ]