# Generated by Django 4.2.13 on 2024-07-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_stock',
            field=models.BooleanField(default=True),
        ),
    ]
