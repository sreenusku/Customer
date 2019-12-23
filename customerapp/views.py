"""
    Views module for our Customerapp.
"""
# django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic.base import View

# local imports
from .utils import render_to_pdf
from .models import Customer
from .forms import CustomerForm


def home(request):
    """
        Here we are fetching all customer details.
    :param request:
    :return: Customer details
    """
    customers = Customer.objects.all()
    return render(request, 'customerapp/home.html', {'customers': customers})


def plain_text_view(request, customer_id):
    """
    Customer details in normal text format.
    :param request:
    :param customer_id: unique id
    :return: single customer details
    """
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'customerapp/plain-text.html', {'customer': customer})


def create_customer(request):
    """
    New customer creation form.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'customerapp/home.html', {})
    else:
        form=CustomerForm()
    return render(request, 'customerapp/create.html', {'form': form})


class GeneratePdf(View):
    """"
    generating Customer details into pdf format.
    """
    model = Customer

    def get(self, request, customer_id, *args, **kwargs):
        from .models import Customer
        customer = get_object_or_404(Customer, pk=customer_id)
        template = get_template('customerapp/invoice.html')
        context = {
            'customer': customer
        }
        html = template.render(context)
        pdf = render_to_pdf('customerapp/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class Generatefoobar(View):
    model = Customer
    pass
