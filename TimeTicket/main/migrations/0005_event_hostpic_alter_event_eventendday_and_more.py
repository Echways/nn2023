# Generated by Django 4.2 on 2023-04-20 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_eventname_event_eventtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hostpic',
            field=models.ImageField(default=0, upload_to='imgs/events/avatars/', verbose_name='Фото организатора'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventendday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 16, 29, 15, 647918), verbose_name='Конец мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventstartday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 16, 29, 15, 647918), verbose_name='Начало мероприятия'),
        ),
    ]