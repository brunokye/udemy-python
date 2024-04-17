import os
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from utils import format
from PIL import Image


class Product(models.Model):
    name = models.CharField(max_length=255)
    description_short = models.TextField(max_length=255)
    description_long = models.TextField()
    image = models.ImageField(
        upload_to="product_images/%Y/%m", null=True, blank=True
    )
    slug = models.SlugField(unique=True, null=True, blank=True)
    price_marketing = models.FloatField(verbose_name="Preço de Venda")
    price_marketing_promotional = models.FloatField(
        default=0, verbose_name="Preço Promocional"
    )
    product_type = models.CharField(
        default="V",
        max_length=1,
        choices=(
            ("V", "Variável"),
            ("S", "Simples"),
        ),
    )

    def get_formated_price(self):
        return format.price_format(self.price_marketing)

    def get_formated_promotional_price(self):
        return format.price_format(self.price_marketing_promotional)

    get_formated_price.short_description = "Preço"
    get_formated_promotional_price.short_description = "Preço Promocional"

    def resize_image(self, image, new_width=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pil = Image.open(image_full_path)
        original_width, original_height = image_pil.size

        if original_width <= new_width:
            image_pil.close()
            return

        new_heigth = round((new_width * original_height) / original_width)
        new_image = image_pil.resize((new_width, new_heigth), Image.LANCZOS)
        new_image.save(image_full_path, optimize=True, quality=60)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

        if self.image:
            self.resize_image(self.image)

    def __str__(self):
        return self.name


class Variation(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    price_promotional = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name
