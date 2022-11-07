from django.contrib import admin
from .models import Table, TableReservation, MenuCategory, Menu

# Register your models here.
admin.site.register(Table)
admin.site.register(TableReservation)
admin.site.register(MenuCategory)
admin.site.register(Menu)

