from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Coupon)
admin.site.register(ProductType)
admin.site.register(Author)
admin.site.register(Product)
admin.site.register(Order)

