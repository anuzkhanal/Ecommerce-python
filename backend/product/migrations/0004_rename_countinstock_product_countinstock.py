# Generated by Django 4.0.2 on 2022-02-26 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='countInstock',
            new_name='countInStock',
        ),
    ]