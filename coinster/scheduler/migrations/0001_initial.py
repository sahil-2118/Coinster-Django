# Generated by Django 4.2.3 on 2023-09-04 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cryptocurrency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_range', models.IntegerField(verbose_name='\n                                               this is time range for store the range of time that user want to send data\n                                               ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('crypto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedulers', to='cryptocurrency.cryptocurrency', verbose_name='the crypto of scheduler')),
            ],
            options={
                'verbose_name_plural': 'schedulers',
                'ordering': ['-created_at'],
            },
        ),
    ]
