from django import forms
from django.contrib.auth import get_user_model

from petstagram_try.photos.models import Photo

UserModel = get_user_model()


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']
