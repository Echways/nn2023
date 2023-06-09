# Generated by Django 4.2 on 2023-04-20 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_event_evemntpic_alter_event_eventendday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventplace',
            field=models.CharField(default='', max_length=100, verbose_name='Место проведения'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventendday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 17, 43, 43, 507461), verbose_name='Конец мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventstartday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 17, 43, 43, 507461), verbose_name='Начало мероприятия'),
        ),
    ]
