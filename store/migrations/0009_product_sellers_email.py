# Generated by Django 3.2.5 on 2021-08-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210830_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sellers_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]