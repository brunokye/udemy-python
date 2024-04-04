import string
from random import SystemRandom
from django.utils.text import slugify


def random_letters(k=5):
    return SystemRandom().choices(string.ascii_letters + string.digits, k=k)


def slugify_new(text, k):
    return slugify(text) + "-" + "".join(random_letters(k))
