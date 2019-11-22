from django.db import models

class Product(models.Model):
    product_options = (
        ('checking', 'CHECKINGS'),
        ('savings', 'SAVINGS'),
        ('credit', 'CREDIT'),
    )

    product_type=models.CharField(
        max_length=12,
        choices=product_options,
        default=product_options[0],
    )