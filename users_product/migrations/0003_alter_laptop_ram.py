# Generated by Django 3.2.5 on 2021-07-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_product', '0002_auto_20210714_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Память процессора'),
        ),
    ]
