# Generated by Django 4.0.1 on 2022-05-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_stocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='product_name'),
        ),
    ]
