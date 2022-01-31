from django.shortcuts import render
from.models import product, TechType, Review
# Create your views here.
def index(request):
    return render(request, 'tech/index.html')
    
def products(request):
    products_list=product.objects.all()
    return render(request, 'tech/products.html',{'product_list: product_list'})
         