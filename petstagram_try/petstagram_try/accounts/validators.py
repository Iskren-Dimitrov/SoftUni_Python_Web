from django.core.exceptions import ValidationError


def alphabetical_letters(value):
    if not value.isalpha():
        raise ValidationError("Use only alphabetical letters")