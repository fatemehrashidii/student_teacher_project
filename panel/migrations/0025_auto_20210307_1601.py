# Generated by Django 3.1.7 on 2021-03-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0024_auto_20210307_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='title',
            field=models.CharField(default=False, max_length=50),
        ),
    ]