# Generated by Django 3.1.7 on 2021-03-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0020_student_student_login_teacher_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_login',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher_login',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
