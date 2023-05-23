from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request=request, template_name='base.html')


def bee_farm(request):
    return render(request=request, template_name='bee_farm.html')