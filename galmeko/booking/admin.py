from django.contrib import admin
from .forms import CustomBookingCreationForm
from django.utils.html import format_html
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site
from booking.models import Booking

class BookingAdmin(admin.ModelAdmin):
    form = CustomBookingCreationForm
    model = Booking
    list_display = ('booking_type', 'origin', 'destination')
    list_filter = ('origin',)
    list_per_page = 5

    fieldsets = (
        (None, {'fields': ('booking_type', 'origin', 'destination')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('booking_type', 'origin', 'destination')}
         ),
    )
    search_fields = ('booking_type',)
    ordering = ('-id',)

admin_site.register(Booking, BookingAdmin)
