"""
    Customerapp django forms.
"""
# django imports
from django import forms

# local imports
from .models import Customer


class CustomerForm(forms.ModelForm):
    """
        Here CustomerForm for Customer model.
    """
    class Meta:
        model = Customer
        fields = "__all__"
