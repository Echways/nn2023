# Generated by Django 3.2.5 on 2023-04-19 08:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230419_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventendday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 11, 18, 0, 575961), verbose_name='Конец мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventstartday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 11, 18, 0, 575961), verbose_name='Начало мероприятия'),
        ),
        migrations.AlterField(
            model_name='productvideo',
            name='video',
            field=models.FileField(upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]