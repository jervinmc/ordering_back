# Generated by Django 4.0.1 on 2022-04-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_transaction_address_transaction_barangay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='subtotal',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='subtotal'),
        ),
    ]
