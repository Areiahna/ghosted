# Generated by Django 3.1 on 2020-08-27 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ghost_app', '0002_auto_20200827_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='post_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
