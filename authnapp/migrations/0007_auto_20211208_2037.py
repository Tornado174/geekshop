# Generated by Django 2.2.24 on 2021-12-08 20:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0006_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 20, 37, 29, 980427, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
