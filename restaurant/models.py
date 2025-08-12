from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Menu table: ID (int(5)), Title (varchar 255), Price (decimal 10,2), Inventory (int(5))
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # int(5) is just a display width in MySQL; we’ll bound the value logically:
    inventory = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )

    def __str__(self):
        return f"{self.title} (${self.price})"


# Booking table: ID (int(11)), Name (varchar 255), No_of_guests (int(6)), BookingDate (datetime)
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999999)]
    )
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} @ {self.booking_date:%Y-%m-%d %H:%M}"
