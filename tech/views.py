from django.shortcuts import render, get_object_or_404
from.models import product, TechType, Review
from django.urls import revers_lazy
# Create your views here.
def index(request):
    return render(request, 'tech/index.html')
    
def products(request):
    products_list=product.objects.all()
    return render(request, 'tech/products.html',{'product_list: product_list'})
def productDetail(request, id):
    product=get_object_or_404(product, pk=id)
    return render(request, 'tech/productdetail.html', {'product' : product} )

         