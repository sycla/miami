from django.contrib import admin
from .models import matchregistration, duomatchregistration, squadmatchregistration
# Register your models here.

admin.site.register(matchregistration)

admin.site.register(duomatchregistration)

admin.site.register(squadmatchregistration)