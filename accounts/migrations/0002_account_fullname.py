# Generated by Django 2.1.3 on 2019-07-12 03:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fullname',
            field=models.CharField(default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
    ]