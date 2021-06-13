from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length = 20)

    class Meta :
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length = 20)
    menu = models.ForeignKey('Menu',on_delete = models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    nutrition = models.ForeignKey("Nutrition", on_delete=models.CASCADE)
    allergy = models.ManyToManyField("Allergy",through = "AllergyProduct")

    class Meta: 
        db_table = 'products'

class Nutrition(models.Model):
    sodium_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    sugars_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    protein_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    caffeine_mg = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        db_table = "nutritions"


class Allergy(models.Model):
    name = models.CharField(max_length =45)

    class Meta: 
        db_table = "allergies"


class AllergyProduct(models.Model):
    product = models.ForeignKey("Product",on_delete=models.CASCADE)
    allery = models.ForeignKey("Allergy",on_delete=models.CASCADE, null = True)

    class Meta:
        db_table = "allergiesproducts"
