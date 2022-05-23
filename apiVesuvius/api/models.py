from django.db import models

# Create your models here.


class Customers(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    phoneNumber = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Tables(models.Model):
    size = models.IntegerField()
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)


class Reservation(models.Model):
    reservation = models.DateTimeField()
    partySize = models.IntegerField()
    tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)
    customerId = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __int__(self):
        return self.partySize


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    amount = models.IntegerField()

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Itemassembly(models.Model):
    menuItemsId = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredientsId = models.ForeignKey(Ingredients, on_delete=models.CASCADE)


class Order(models.Model):
    tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)


class OrderItems(models.Model):
    menuItemsId = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)


class Table_list(models.Model):
    tableId = models.ForeignKey(Tables, on_delete=models.CASCADE)
    reservationId = models.ForeignKey(Reservation, on_delete=models.CASCADE)