# Generated by Django 4.2.3 on 2023-08-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocurrency', '0003_cryptocurrency_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='volume_24h',
            field=models.BigIntegerField(),
        ),
    ]