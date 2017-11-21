# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalorieTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddescription',
            name='cho_factor',
            field=models.DecimalField(blank=True, null=True, help_text='Factor for calculating calories from carbohydrate (see p. 14).', max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='fooddescription',
            name='com_name',
            field=models.CharField(max_length=100, blank=True, null=True, help_text='Other names commonly used to describe a food, including local or regional names for various foods, for example, “soda” or “pop” for “carbonated beverages.”'),
        ),
        migrations.AddField(
            model_name='fooddescription',
            name='fat_factor',
            field=models.DecimalField(blank=True, null=True, help_text='Factor for calculating calories from fat (see p. 14).', max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='fooddescription',
            name='long_desc',
            field=models.CharField(max_length=200, null=True, help_text='200-character description of food item.'),
        ),
        migrations.AddField(
            model_name='fooddescription',
            name='manufacturer_name',
            field=models.CharField(max_length=65, blank=True, null=True, help_text='Indicates the company that manufactured the product, when appropriate.'),
        ),
        migrations.AddField(
            model_name='fooddescription',
            name='short_desc',
            field=models.CharField(max_length=60, null=True, help_text='60-character abbreviated description of food item. Generated from the 200-character description using abbreviations in Appendix A. If short description is longer than 60 characters, additional abbreviations are made.'),
        ),
        migrations.AlterField(
            model_name='fooddescription',
            name='protein_factor',
            field=models.IntegerField(null=True, help_text='Factor for calculating calories from protein (see p. 14).'),
        ),
    ]
