from django.db import models
from django.utils.translation import gettext_lazy as _
from os import path


def upload_to(instance, filename):
    name_to_path = str(instance.id)
    print(instance.id)
    new_path = path.join('files',
                         # "media", filename)
                         name_to_path,
                         filename)
    print(new_path)
    return new_path

# Create your models here.
class LinksModel(models.Model):
    number = models.IntegerField(verbose_name="Порядковый номер", null=True, blank=True, unique=True)
    name = models.CharField(verbose_name="Название", null=True, blank=True, max_length=15)
    image = models.ImageField(verbose_name="Изображение", null=True, blank=True,
                              upload_to=upload_to)
    link = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name = _("ссылка")
        verbose_name_plural = _("ссылки")

    def __str__(self):
        return f'{self.number} - {self.name}'

