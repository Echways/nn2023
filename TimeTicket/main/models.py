from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Event(models.Model):
    eventname = models.CharField('Название мероприятия', max_length=100, default="")
    eventstartday = models.DateTimeField('Начало мероприятия', default=datetime.now())
    eventendday = models.DateTimeField('Конец мероприятия', default=datetime.now())
    eventdescription = models.CharField('Описание мероприятия', max_length=500, default="")
    ticketprice = models.IntegerField('Цена билета', default=0)
    eventminage = models.IntegerField('Минимальный возраст для посещения', default=0)
    evemntpic = models.ImageField('Промо-фото', upload_to='imgs/events/', default=0)
    ticket = models.ImageField('Билет', upload_to='imgs/events/', default=0)
    hostname = models.SlugField('Организатор', max_length=100, default="", allow_unicode=1)
    hostemail = models.EmailField('Почта организатора', max_length=100, default="")
    hosttg = models.CharField('Телеграм организатора', max_length=100, default="")

    def __str__(self):
        return self.eventname

    def get_absolute_url(self):
        return reverse('main', kwargs={'pk': self.pk})


class ProductVideo(models.Model):
    video = models.FileField(upload_to='video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    product = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='File')


class RegisterEvent(models.Model):
    name = models.CharField('Имя', max_length=100, default="")
    surname = models.CharField('Фамилия', max_length=100, default="")
    email = models.EmailField('Ваша почта', max_length=100, default="")
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='RegisterEvent')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobileph = models.IntegerField()
    email = models.EmailField()
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
