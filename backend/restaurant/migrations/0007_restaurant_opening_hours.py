# Generated by Django 3.2 on 2021-07-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_restaurant_price_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='opening_hours',
            field=models.CharField(default='', max_length=50),
        ),
    ]
