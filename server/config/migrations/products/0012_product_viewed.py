# Generated by Django 3.1.4 on 2021-01-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210114_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='viewed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
