# Generated by Django 2.1.3 on 2019-07-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='pid',
            field=models.IntegerField(),
        ),
    ]
