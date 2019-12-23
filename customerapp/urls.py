"""
    Customerapp URLs and Endpoints.
"""
# django imports
from django.urls import path

# local imports
from .views import (home,
                    plain_text_view,
                    GeneratePdf,
                    create_customer,)

urlpatterns = [
    path('', home, name='home'),
    path('<int:customer_id>/', plain_text_view, name='plain-text'),
    path('<int:customer_id>/pdf/', GeneratePdf.as_view(), name='invoice'),
    path('create/', create_customer, name='create'),
]
