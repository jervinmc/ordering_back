# Generated by Django 4.0.1 on 2022-04-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='age'),
        ),
        migrations.AddField(
            model_name='user',
            name='barangay',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='barangay'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='number'),
        ),
        migrations.AddField(
            model_name='user',
            name='province',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='province'),
        ),
    ]
