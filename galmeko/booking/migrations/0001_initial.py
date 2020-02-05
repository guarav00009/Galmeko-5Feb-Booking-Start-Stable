# Generated by Django 3.0.2 on 2020-02-05 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setting', '0002_features'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.IntegerField(choices=[(1, 'Hospital'), (3, 'User')], default=1, verbose_name='status')),
                ('origin', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('booking_msg', models.TextField()),
                ('round_trip', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('fare', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.VehicleCategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.Vehicle')),
            ],
            options={
                'verbose_name': 'Bookings',
                'verbose_name_plural': 'Bookings',
                'db_table': 'bookings',
            },
        ),
    ]
