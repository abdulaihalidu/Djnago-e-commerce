# Generated by Django 3.2.5 on 2021-09-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_sellers_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
