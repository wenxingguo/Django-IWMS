# Generated by Django 3.0.4 on 2020-04-06 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='current',
            old_name='Current_value',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='poolimg',
            old_name='image',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='sound',
            old_name='Sound_value',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='voltage',
            old_name='Voltage_value',
            new_name='value',
        ),
    ]
