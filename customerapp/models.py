"""
    Db models and fields for Customerapp.
"""
# django imports
from django.db import models


class Customer(models.Model):
    """
        Customer table fields.
    """
    name = models.CharField(max_length=100)
    mob_num = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
