from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})


class FoodDescription(models.Model):
    long_desc = models.CharField(max_length=200, null=True, help_text='200-character description of food item.')
    short_desc = models.CharField(max_length=60, null=True, help_text='60-character abbreviated description of food item. Generated from the 200-character description using abbreviations in Appendix A. If short description is longer than 60 characters, additional abbreviations are made.')
    com_name = models.CharField(max_length=100, null=True, blank=True, help_text='Other names commonly used to describe a food, including local or regional names for various foods, for example, “soda” or “pop” for “carbonated beverages.”')
    manufacturer_name = models.CharField(max_length=65, null=True, blank=True, help_text='Indicates the company that manufactured the product, when appropriate.')
    protein_factor = models.IntegerField(null=True, help_text='Factor for calculating calories from protein (see p. 14).')
    fat_factor = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text='Factor for calculating calories from fat (see p. 14).')
    cho_factor = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text='Factor for calculating calories from carbohydrate (see p. 14).')


    def get_absolute_url(self):
        return reverse('fooddescription_edit', kwargs={'pk': self.pk})




# class NutrientDefinition(models.Model):
#     nutrient_number = models.CharField(primary_key=True, max_length=3, help_text='Unique 3-digit identifier code for a nutrient.')
#     units = models.CharField(max_length=7, help_text='Units of measure (mg, g, μg, and so on).')
#     tagname = models.CharField(max_length=20, blank=True, null=True, help_text='International Network of Food Data Systems (INFOODS) Tagnames.† A unique abbreviation for a nutrient/food component developed by INFOODS to aid in the interchange of data.')
#     nutrient_description = models.CharField(max_length=60, help_text='Name of nutrient/food component.')
#     num_decimal_places = models.CharField(max_length=1, help_text='Number of decimal places to which a nutrient value is rounded.')
#     sort_order = models.PositiveSmallIntegerField(help_text='Used to sort nutrient records in the same order as various reports produced from SR.')
#
#     def __str__(self):
#         return self.nutrient_description
#

# class NutrientData(models.Model):
#     food_description = models.ForeignKey(FoodDescription, related_name='nutrient_data', help_text='5-digit Nutrient Databank number that uniquely identifies a food item. If this field is defined as numeric, the leading zero will be lost.')
#     nutrient_definition = models.ForeignKey(NutrientDefinition, help_text='Unique 3-digit identifier code for a nutrient.')
#     nutrient_value = models.DecimalField(max_digits=13, decimal_places=3, help_text='Amount in 100 grams, edible portion. (Nutrient values have been rounded to a specified number of decimal places for each nutrient. Number of decimal places is listed in the Nutrient Definition file.)')
#     number_data_points = models.PositiveSmallIntegerField(help_text='Number of data points is the number of analyses used to calculate the nutrient value. If the number of data points is 0, the value was calculated or imputed.')
#     standard_error = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True, help_text='Standard error of the mean. Null if cannot be calculated. The standard error is also not given if the number of data points is less than three.')
#     ref_food_description = models.ForeignKey(FoodDescription, blank=True, null=True, help_text='NDB number of the item used to calculate a missing value. Populated only for items added or updated starting with SR14.')
#     add_nutr_mark = models.NullBooleanField(help_text='Indicates a vitamin or mineral added for fortification or enrichment. This field is populated for ready-to- eat breakfast cereals and many brand-name hot cereals in food group 08.')
#     num_studies = models.PositiveSmallIntegerField(null=True, blank=True, help_text='Number of studies.')
#     minimum = models.DecimalField(max_digits=13, decimal_places=3, help_text='Minimum value.')
#     maximum = models.DecimalField(max_digits=13, decimal_places=3, help_text='Maximum value.')
#     degrees_of_freedom = models.PositiveSmallIntegerField(null=True, blank=True, help_text='Degrees of freedom.')
#     lower_error_bound = models.DecimalField(max_digits=13, decimal_places=3, help_text='Lower 95% error bound.')
#     upper_error_bound = models.DecimalField(max_digits=13, decimal_places=3, help_text='Upper 95% error bound.')
#     statistical_comments = models.CharField(max_length=10, null=True, blank=True, help_text='Statistical comments. See definitions below.')
#     modified_date = models.CharField(max_length=10, null=True, blank=True, help_text='Indicates when a value was either added to the database or last modified.')
#     confidence_code = models.CharField(max_length=1, null=True, blank=True, help_text='Confidence Code indicating data quality, based on evaluation of sample plan, sample handling, analytical method, analytical quality control, and number of samples analyzed. Not included in this release, but is planned for future releases.')


class Day(models.Model):
    date_created = models.DateField()


class Entry(models.Model):
    proner = models.IntegerField()
