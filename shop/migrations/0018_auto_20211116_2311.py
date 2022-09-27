# Generated by Django 3.2.9 on 2021-11-16 17:41

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20211112_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Price (in Rupees)'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Sub Category'),
        ),
    ]
