# Generated by Django 3.2.5 on 2021-08-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='allowed4shipping',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
