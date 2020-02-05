# Generated by Django 3.0.2 on 2020-02-05 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_emailtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Pending'), (3, 'Deleted')], default=1, verbose_name='status'),
        ),
    ]
