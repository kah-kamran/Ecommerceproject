# Generated by Django 3.2.9 on 2021-12-13 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
