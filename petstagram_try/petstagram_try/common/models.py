from django.contrib.auth import get_user_model
from django.db import models

from petstagram_try.accounts.models import PetstagramUser
from petstagram_try.photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField(
        blank=False,
        null=False,
        max_length=300,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now=True,
    )

    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    user = models.ForeignKey(PetstagramUser, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-date_time_of_publication"]


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE

    )

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE
    )
