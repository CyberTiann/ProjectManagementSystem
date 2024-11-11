from django import template

register = template.Library()

@register.filter
def dictget(value, arg):
    return next((item for item in value if item.id == arg), None)

@register.filter
def attr(obj, attr):
    return getattr(obj, attr)