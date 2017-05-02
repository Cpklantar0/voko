# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0070_auto_20161024_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Bestelling', 'verbose_name_plural': 'Bestellingen'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Productbestelling', 'verbose_name_plural': 'Productbestellingen'},
        ),
        migrations.AlterModelOptions(
            name='orderproductcorrection',
            options={'verbose_name': 'Productbestelling-correctie', 'verbose_name_plural': 'Productbestelling-correcties'},
        ),
        migrations.AlterModelOptions(
            name='orderround',
            options={'verbose_name': 'Bestelronde', 'verbose_name_plural': 'Bestelronden'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Producten'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Leverancier'},
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='amount',
            field=models.IntegerField(verbose_name='Aantal'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='base_price',
            field=models.DecimalField(decimal_places=2, help_text='The price the product was bought for', max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='retail_price',
            field=models.DecimalField(decimal_places=2, help_text='The price the product was sold for', max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderproductcorrection',
            name='charge_supplier',
            field=models.BooleanField(default=True, verbose_name='Charge expenses to supplier'),
        ),
        migrations.AlterField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False, verbose_name="Show 'new' label"),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_amount',
            field=models.IntegerField(default=1, help_text='e.g. if half a kilo: "500"'),
        ),
        migrations.AlterField(
            model_name='productstock',
            name='type',
            field=models.CharField(choices=[('added', 'Added'), ('lost', 'Lost')], db_index=True, default='added', max_length=5),
        ),
        migrations.AlterField(
            model_name='productunit',
            name='abbreviations',
            field=models.CharField(blank=True, help_text='whitespace separated', max_length=255),
        ),
    ]
