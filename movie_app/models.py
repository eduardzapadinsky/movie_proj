from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    # slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('director-detailed', args=[self.id])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.last_name, allow_unicode=True)
    #     super(Director, self).save(*args, **kwargs)


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.floor} - {self.number}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Чоловік'),
        (FEMALE, 'Жінка'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актор {self.first_name} {self.last_name}'
        else:
            return f'Акторка {self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('actor-detailed', args=[self.id])


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    UAH = 'UAH'
    CURRENCY_CHOICES = [
        (USD, 'Dollar'),
        (EUR, 'Euro'),
        (UAH, 'Uah'),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=UAH)
    slug = models.SlugField(default='', null=False, db_index=True, unique=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detailed', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'

# manage.py makemigrations
# Make inside migrations

# manage.py migrate
# write migrtations inyo sql db

# manage.py shell_plus --print-sql
# work with sql

# from movie_app.models import Movie

# Movie.objects.all()
# Select from db

# <change>.save()
# save changes into db

# from django.db.models import Q
