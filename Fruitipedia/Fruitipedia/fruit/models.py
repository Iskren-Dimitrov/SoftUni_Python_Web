from django.core.validators import MinLengthValidator
from django.db import models

from Fruitipedia.fruit.validators import check_first_name_capital_letter, check_last_name_capital_letter, \
    plant_name_only_letters


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), check_first_name_capital_letter],
    )

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1), check_last_name_capital_letter],
    )

    email = models.CharField(
        max_length=40,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(8)],
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        default=18,
    )


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), plant_name_only_letters],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=False,
        blank=False,
    )
