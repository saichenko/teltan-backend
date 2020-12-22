# Generated by Django 3.1.4 on 2020-12-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary_objects', '0002_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Code'),
        ),
    ]
