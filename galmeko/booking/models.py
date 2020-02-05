from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
User = settings.AUTH_USER_MODEL
from setting.models import Vehicle,VehicleCategory

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = (
    (1, 'Hospital'),
    (3, 'User'),
    )
    booking_type = models.IntegerField(
    _('status'), choices=STATUS_CHOICES, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    origin = models.CharField(max_length=20, blank=False, null=False)
    destination = models.CharField(max_length=20, blank=False, null=False)
    booking_msg = models.TextField()
    round_trip = models.BooleanField(default=False)
    category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    fare = models.DecimalField(max_digits=6, decimal_places=2) 
    date = models.DateField()

    class Meta:
        db_table = "bookings"
        verbose_name = 'Bookings'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.booking_type