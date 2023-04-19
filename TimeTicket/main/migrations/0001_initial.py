# Generated by Django 4.2 on 2023-04-19 10:39

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(default='', max_length=100, verbose_name='Название мероприятия')),
                ('eventstartday', models.DateTimeField(default=datetime.datetime(2023, 4, 19, 13, 39, 22, 223807), verbose_name='Начало мероприятия')),
                ('eventendday', models.DateTimeField(default=datetime.datetime(2023, 4, 19, 13, 39, 22, 223807), verbose_name='Конец мероприятия')),
                ('eventdescription', models.CharField(default='', max_length=500, verbose_name='Описание мероприятия')),
                ('ticketprice', models.IntegerField(default=0, verbose_name='Цена билета')),
                ('eventminage', models.IntegerField(default=0, verbose_name='Минимальный возраст для посещения')),
                ('evemntpic', models.ImageField(default=0, upload_to='imgs/events/', verbose_name='Промо-фото')),
                ('hostname', models.SlugField(allow_unicode=1, default='', max_length=100, verbose_name='Организатор')),
                ('hostemail', models.EmailField(default='', max_length=100, verbose_name='Почта организатора')),
                ('hosttg', models.CharField(default='', max_length=100, verbose_name='Телеграм организатора')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileph', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='File', to='main.event')),
            ],
        ),
    ]
