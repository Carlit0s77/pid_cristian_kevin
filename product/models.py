from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product name')
    description = models.CharField(max_length=300, null= True, verbose_name='Product description')
    price = models.FloatField(null=False, blank=False, verbose_name='Product value')
    created = models.DateField(auto_now_add=True, verbose_name='Created')
