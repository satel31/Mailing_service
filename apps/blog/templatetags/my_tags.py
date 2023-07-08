from django import template

register = template.Library()

@register.filter
def mediapath(photo_path):
    if photo_path:
        return f'/media/{photo_path}'
    else:
        return None
