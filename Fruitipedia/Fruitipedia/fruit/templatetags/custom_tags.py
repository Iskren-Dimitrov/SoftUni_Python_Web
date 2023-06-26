from django import template

from Fruitipedia.fruit.models import Profile

register = template.Library()


@register.simple_tag()
def get_profile():
    return Profile.objects.first()
