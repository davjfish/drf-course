from django.contrib import admin

# Register your models here.
from .models import Ebook, Review

admin.site.register(Ebook)
admin.site.register(Review)