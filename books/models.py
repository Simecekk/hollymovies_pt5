from django.db import models
from django.shortcuts import resolve_url

from movies.models import BasePersonModel


class Author(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('author_detail', pk=self.pk)


class Book(models.Model):
    GENRE_HORROR = 'horror'
    GENRE_DRAMA = 'drama'

    GENRE_CHOICES = (
        (GENRE_HORROR, 'horror'),
        (GENRE_DRAMA, 'drama'),
    )

    title = models.CharField(max_length=256)
    number_of_pages = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICES, max_length=256)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        related_name='books',
        null=True, blank=True,
    )
    released_at = models.DateField()
