# Generated by Django 5.1.4 on 2024-12-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0003_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]