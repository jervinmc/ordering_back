# Generated by Django 4.0.1 on 2022-05-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_alter_transaction_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='users_profile',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='users_profile'),
        ),
    ]