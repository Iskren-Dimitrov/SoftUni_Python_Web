from django.core.validators import MinLengthValidator
from django.db import models

from plants_try.web.validators import validate_first_last_name, letters_validator


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        validators=[MinLengthValidator(2)],
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[validate_first_last_name],
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[validate_first_last_name],

    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Plant(models.Model):
    CHOICES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    plant_type = models.CharField(
        blank=False,
        null=False,
        max_length=14,
        choices=CHOICES,

    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[MinLengthValidator(2), letters_validator],
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )
