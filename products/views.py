from django.shortcuts import render

from basic_dtl_project_bee_farm_website.products.forms import PaymentForm
from basic_dtl_project_bee_farm_website.products.models import Products


# Create your views here.
def all_products(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request=request, template_name='products.html', context=context)


def buy_product(request):

    return render(request=request, template_name='payment.html', context={"form": PaymentForm})