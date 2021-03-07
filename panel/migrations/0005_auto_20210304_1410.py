# Generated by Django 3.1.7 on 2021-03-04 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20210304_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_exercises',
            old_name='date_time',
            new_name='deadline',
        ),
        migrations.RemoveField(
            model_name='watching_videos',
            name='dete_time',
        ),
        migrations.AddField(
            model_name='sending_response',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]