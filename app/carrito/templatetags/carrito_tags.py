from django import template

register = template.Library()


@register.filter()
def multiply(arg, value):
    return float(arg) * value


@register.filter()
def money_format(arg, value):
    return f"{arg}{value}"
