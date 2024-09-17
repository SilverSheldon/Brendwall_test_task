from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, DecimalValidator
from django.urls import reverse_lazy


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена",
        validators=[
            MinValueValidator(limit_value=Decimal('0.009'), message="Цена должна быть положительной!"),
        ]
    )

    objects = models.Manager()

    class Meta:
        ordering = ['title']
        indexes = [models.Index(fields=['title'])]
        verbose_name = "ПРОДУКТ"
        verbose_name_plural = "ПРОДУКТЫ"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('shop:add_product', kwargs={})
