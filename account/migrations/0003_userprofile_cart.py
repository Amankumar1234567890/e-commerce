# Generated by Django 3.2.8 on 2021-10-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211012_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cart',
            field=models.JSONField(blank=True, default=None, verbose_name='Cart'),
            preserve_default=False,
        ),
    ]