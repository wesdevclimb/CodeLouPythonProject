# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('proner', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('long_desc', models.CharField(max_length=200, null=True, help_text='200-character description of food item.')),
                ('short_desc', models.CharField(max_length=60, null=True, help_text='60-character abbreviated description of food item. Generated from the 200-character description using abbreviations in Appendix A. If short description is longer than 60 characters, additional abbreviations are made.')),
                ('com_name', models.CharField(max_length=100, blank=True, null=True, help_text='Other names commonly used to describe a food, including local or regional names for various foods, for example, “soda” or “pop” for “carbonated beverages.”')),
                ('manufacturer_name', models.CharField(max_length=65, blank=True, null=True, help_text='Indicates the company that manufactured the product, when appropriate.')),
                ('protein_factor', models.IntegerField(null=True, help_text='Factor for calculating calories from protein (see p. 14).')),
                ('fat_factor', models.DecimalField(blank=True, null=True, help_text='Factor for calculating calories from fat (see p. 14).', max_digits=6, decimal_places=2)),
                ('cho_factor', models.DecimalField(blank=True, null=True, help_text='Factor for calculating calories from carbohydrate (see p. 14).', max_digits=6, decimal_places=2)),
            ],
        ),
    ]
