# Generated by Django 3.2.9 on 2021-11-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
