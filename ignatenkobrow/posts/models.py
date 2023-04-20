from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


User = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Services(models.Model):
    procedure = models.CharField('Названия', max_length=32)
    price = models.IntegerField('Цена')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('price123')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Blog(models.Model):
    name_blog = models.CharField('Названия', max_length=30)
    main_text = models.TextField()
    pub_date = models.DateTimeField("data published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
