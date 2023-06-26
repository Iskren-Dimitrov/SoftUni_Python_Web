from django.core.exceptions import ValidationError


def check_first_name_capital_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def check_last_name_capital_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def plant_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')
