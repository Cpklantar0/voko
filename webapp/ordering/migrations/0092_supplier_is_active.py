# Generated by Django 3.2.20 on 2024-02-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0091_auto_20230213_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
