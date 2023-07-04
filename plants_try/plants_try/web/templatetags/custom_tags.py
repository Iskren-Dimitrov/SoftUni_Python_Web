from django import template

from plants_try.web.models import Profile

register = template.Library()


@register.simple_tag
def get_profile():
    return Profile.objects.first()
