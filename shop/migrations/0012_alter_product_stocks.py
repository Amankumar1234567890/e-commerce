# Generated by Django 3.2.8 on 2021-10-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stocks',
            field=models.IntegerField(blank=True, null=True, verbose_name='Stocks Left'),
        ),
    ]