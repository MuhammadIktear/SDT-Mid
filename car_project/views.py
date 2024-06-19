from django.shortcuts import render
from Car.models import Car, Brand

def home(request, brand_slug=None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug=brand_slug)
        data = data.filter(brand=brand)
    data2 = Brand.objects.all()
    return render(request, 'home.html', {'cars': data, 'brands': data2})
