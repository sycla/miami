from django.contrib import admin

from .models import jetski, ponton, yacht

# Register your models here.
admin.site.register(jetski)

admin.site.register(ponton)

admin.site.register(yacht)