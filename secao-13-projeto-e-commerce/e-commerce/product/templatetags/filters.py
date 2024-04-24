from django.template import Library
from utils import format

register = Library()


@register.filter
def price_format(value):
    return format.price_format(value)


@register.filter
def cart_total_qtt(cart):
    return format.cart_total_qtt(cart)
