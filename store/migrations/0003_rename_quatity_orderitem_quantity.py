# Generated by Django 3.2.5 on 2021-08-14 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
