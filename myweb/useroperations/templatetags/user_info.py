from django import template
from django.contrib.auth.models import User
register = template.Library()

@register.simple_tag
def get_nickname_or_username(user):
    try:
        name = user.userprofile.nickname
    except User.userprofile.RelatedObjectDoesNotExist :
        name = user.username
    return name