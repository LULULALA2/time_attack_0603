# Generated by Django 4.0.5 on 2022-06-03 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='allergy',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='nutrition_info',
        ),
    ]
