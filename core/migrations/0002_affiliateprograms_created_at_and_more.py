# Generated by Django 4.1.4 on 2022-12-26 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliateprograms',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='affiliateprograms',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
