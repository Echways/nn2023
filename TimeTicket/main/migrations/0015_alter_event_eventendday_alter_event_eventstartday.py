# Generated by Django 4.2 on 2023-04-20 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_event_eventendday_alter_event_eventstartday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventendday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 1, 12, 50, 770826), verbose_name='Конец мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventstartday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 1, 12, 50, 770826), verbose_name='Начало мероприятия'),
        ),
    ]
