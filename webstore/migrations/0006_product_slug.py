# Generated by Django 5.1.4 on 2024-12-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
