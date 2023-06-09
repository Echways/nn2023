# Generated by Django 4.2 on 2023-04-20 09:58

import datetime
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='password2',
        ),
        migrations.AlterField(
            model_name='event',
            name='eventendday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 12, 58, 4, 694234), verbose_name='Конец мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventstartday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 12, 58, 4, 694234), verbose_name='Начало мероприятия'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
