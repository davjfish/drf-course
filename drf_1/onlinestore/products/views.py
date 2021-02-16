from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from .models import Product, Manufacturer


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    data = {
        "products": list(products.values())
    }
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "price": product.price,
                "photo": product.photo.url,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
            }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        data = {
            "error": {
                "code": 404,
                "message": "product not found!",
            }}
        response = JsonResponse(data, status=404)
    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {
        "manufacturers": list(manufacturers.values())
    }
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "manufacturer": manufacturer.location,
                "active": manufacturer.active,
            }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        data = {
            "error": {
                "code": 404,
                "message": "manufacturer not found!",
            }}
        response = JsonResponse(data, status=404)
    return response



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
