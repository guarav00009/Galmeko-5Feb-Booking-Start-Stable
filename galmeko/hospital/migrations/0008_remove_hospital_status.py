# Generated by Django 3.0.2 on 2020-02-05 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_remove_hospital_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='status',
        ),
    ]
