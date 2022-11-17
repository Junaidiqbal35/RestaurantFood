# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from fieldsignals import pre_save_changed


class MenuCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Menu(models.Model):
    menu_name = models.CharField(max_length=255)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='category_menu')
    recipe_name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)

    def __str__(self):
        return f'{self.recipe_name} price is {self.price}'


class Table(models.Model):
    table_number = models.CharField(max_length=20)
    seating_capacity = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return f'Table {self.table_number} have seating capacity of {self.seating_capacity}'


class TableReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=355)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_date = models.DateField(blank=False)
    start_time = models.TimeField(auto_now_add=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Table Number {self.table}. Booked by {self.user}' \
               f'people, for the {self.booking_date} at {self.start_time}. Status {self.approved}'



