from django.conf import settings
from django.db import models


# Create your models here.


class Column(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя поля')
    width = models.PositiveIntegerField(verbose_name='Ширина')

    def __str__(self):
        return f'{self.name} {self.width}'


class FilePath(models.Model):
    path = models.FilePathField(path=settings.BASE_DIR, verbose_name='Путь к csv файлу')

    def get_path(self):
        return self.path

    def set_path(self, new_path):
        self.path = new_path
