from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=200
    )
    short_description = models.TextField(
        'Краткое описание',
        blank=True
    )
    long_description = HTMLField(
        'полное описание',
        blank=True,
    )
    lat = models.FloatField(
        'Широта'
    )
    lng = models.FloatField(
        'Долгота'
    )

    class Meta:
        unique_together = [['title', 'short_description']]

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField(
        'Фотография'
    )
    sequence_number = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name='Порядковый номер',
    )

    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return f'{self.sequence_number} {self.place}'
