# Generated by Django 4.0.1 on 2022-05-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_transaction_users_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='color'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='size'),
        ),
    ]
