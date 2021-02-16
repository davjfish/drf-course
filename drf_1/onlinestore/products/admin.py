from django.contrib import admin

# Register your models here.
from .models import  Manufacturer, Product
admin.site.register(Manufacturer)
admin.site.register(Product)