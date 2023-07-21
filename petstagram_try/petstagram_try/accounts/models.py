from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_try.accounts.validators import alphabetical_letters


class ChoicesMixin:

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringsMixin, Enum):
    Male = 'male'
    Female = 'female'
    DO_NOT_SHOW = 'do not show'


class PetstagramUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(MinLengthValidator(2), alphabetical_letters,)
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(MinLengthValidator(2), alphabetical_letters,)
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,

    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_length(),
    )

    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name

        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username


# class Photo(models.Model):
#     user = models.ForeignKey(PetstagramUser, on_delete=models.CASCADE)
