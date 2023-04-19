# Generated by Django 3.2.5 on 2023-04-19 06:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_evemntpic_alter_event_eventendday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventendday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 9, 34, 38, 324072), verbose_name='Конец мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventstartday',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 9, 34, 38, 324072), verbose_name='Начало мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hostname',
            field=models.SlugField(allow_unicode=1, default='', max_length=100, verbose_name='Организатор'),
        ),
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/%Y/%m/%d')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event')),
            ],
        ),
    ]
