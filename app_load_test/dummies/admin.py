from django.contrib import admin
from .models import Dummies

@admin.register(Dummies)
class DummiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'height', 'weight')
