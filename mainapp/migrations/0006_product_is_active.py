# Generated by Django 2.2.24 on 2021-11-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_auto_20211116_2215"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="продукт активен"),
        ),
    ]
