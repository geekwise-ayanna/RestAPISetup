from django.contrib import admin
from drf.account import Account
from drf.product import Product
from drf.customer import Customer

# Register your models here.
admin.site.Register(Account)
admin.site.Register(Product)
admin.site.Register(Customer)
