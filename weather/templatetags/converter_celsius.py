from django import template

register = template.Library()

@register.filter(name='converter')
def converter(value):
    celsius = value - 273
    return round(celsius)