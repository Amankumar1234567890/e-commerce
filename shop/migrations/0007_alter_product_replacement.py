# Generated by Django 3.2.8 on 2021-10-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20211016_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='replacement',
            field=models.CharField(blank=True, default='No', max_length=20, verbose_name='Replacement'),
        ),
    ]