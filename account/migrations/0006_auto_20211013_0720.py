# Generated by Django 3.2.8 on 2021-10-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_userprofile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.JSONField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cart',
            field=models.JSONField(blank=True, null=True, verbose_name='Cart'),
        ),
    ]
