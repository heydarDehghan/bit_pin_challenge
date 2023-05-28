from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Rating(models.Model):

    # ↓ Actual value
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    RATE_CHOOSE = [      # ↓ Displayed on Django Admin
        (ZERO, 'zero'),
        (ONE, 'one'),
        (TWO, 'two'),
        (THREE, 'three'),
        (FOUR, 'four'),
        (FIVE, 'five'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.CharField(
        max_length=1,
        choices=RATE_CHOOSE,
        default=FIVE
    )
    def __str__(self):
        return self.product.title