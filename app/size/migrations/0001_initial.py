# Generated by Django 4.0.1 on 2022-05-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True, verbose_name='product_id')),
                ('label', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_id')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]