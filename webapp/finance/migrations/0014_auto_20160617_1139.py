# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-17 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0013_auto_20160617_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='transaction_code',
            new_name='qantani_transaction_code',
        ),
    ]
