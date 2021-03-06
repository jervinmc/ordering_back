# Generated by Django 4.0.1 on 2022-04-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='tattoo_name')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='price')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='user_id')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='quantity')),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
