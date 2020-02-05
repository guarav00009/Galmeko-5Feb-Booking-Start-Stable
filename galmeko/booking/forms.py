from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from booking.models import Booking

class CustomBookingCreationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_type', 'origin', 'destination')