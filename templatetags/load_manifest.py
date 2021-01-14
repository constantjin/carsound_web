from django import template
from django.conf import settings

register = template.Library()


@register.filter
def load_manifest(mapping, key):
    return settings.STATIC_URL + mapping.get(key, "").get("file")
