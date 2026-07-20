from django.db import models
from django.shortcuts import render, get_object_or_404

# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   reservation_time = models.DateTimeField(auto_now_add=True)
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Create Menu model
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name

def display_menu_item(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk)

    return render(
        request,
        "menu_item.html",
        {"menu_item": menu_item}
    )