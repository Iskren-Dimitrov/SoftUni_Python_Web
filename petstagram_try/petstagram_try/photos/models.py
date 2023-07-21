from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_try.pets.models import Pet
from petstagram_try.photos.validators import validate_file_size

UserModel = get_user_model()

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='images',
        blank=False,
        null=False,
        validators=[validate_file_size]
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        validators=[MinLengthValidator(10)],

    )

    location = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        blank=False,
        null=False,
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE
    )