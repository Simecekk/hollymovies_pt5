from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BasePersonModel(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    name = models.CharField(max_length=256)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    born_at = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Actor(BasePersonModel):
    pass


class Director(BasePersonModel):
    pass


class Movie(models.Model):
    LANGUAGE_ENG = 'eng'
    LANGUAGE_CZ = 'cz'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, 'english'),
        (LANGUAGE_CZ, 'czech'),
    )

    name = models.CharField(max_length=256)
    description = models.TextField()
    rating = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    released = models.DateField()
    actors = models.ManyToManyField('Actor', related_name='movies')
    director = models.ForeignKey(
        'Director',
        on_delete=models.PROTECT,
        related_name='movies',
        null=True, blank=True,
    )

    def __str__(self):
        return f'{self.name} : {self.id}'
