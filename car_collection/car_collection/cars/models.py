from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection.cars.validators import raise_error_of_minimum_characters, year_validation


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), raise_error_of_minimum_characters],

    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(18)],
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,

    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),

    )

    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CHOICES,
    )

    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)],
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[year_validation],

    )

    image_url = models.URLField(
        blank=False,
        null=False,

    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1)],
    )
