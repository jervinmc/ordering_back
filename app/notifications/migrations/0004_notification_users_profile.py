# Generated by Django 4.0.1 on 2022-05-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='users_profile',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='users_profile'),
        ),
    ]