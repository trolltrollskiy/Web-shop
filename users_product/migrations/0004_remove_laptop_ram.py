# Generated by Django 3.2.5 on 2021-07-14 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_product', '0003_alter_laptop_ram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='ram',
        ),
    ]
