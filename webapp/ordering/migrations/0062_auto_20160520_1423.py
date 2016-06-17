# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-20 12:23
from __future__ import unicode_literals

from django.db import migrations


def copy_base_prices(apps, _):
    OrderProduct = apps.get_model("ordering", "OrderProduct")

    for odp in OrderProduct.objects.all():
        odp.base_price = odp.product.base_price
        odp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0061_orderproduct_base_price'),
    ]

    operations = [
        migrations.RunPython(copy_base_prices)
    ]