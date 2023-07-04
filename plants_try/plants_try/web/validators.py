from django.core.exceptions import ValidationError


def validate_first_last_name(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def letters_validator(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")