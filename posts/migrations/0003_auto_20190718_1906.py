# Generated by Django 2.1.3 on 2019-07-18 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190718_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 19, 6, 22, 633985), max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.TextField(max_length=100),
        ),
    ]