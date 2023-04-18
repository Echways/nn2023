# Generated by Django 4.2 on 2023-04-18 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_event_name_event_eventdescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='evemntpic',
            field=models.ImageField(default=0, upload_to='imgs/events/', verbose_name='Промо-фото'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventendday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 15, 48, 49, 828370), verbose_name='Конец мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventstartday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 15, 48, 49, 828370), verbose_name='Начало мероприятия'),
        ),
    ]
