# Generated by Django 3.0.5 on 2020-05-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20200515_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='address',
            field=models.CharField(default='dummy', max_length=100),
        ),
    ]
