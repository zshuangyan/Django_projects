# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-05 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_order_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]