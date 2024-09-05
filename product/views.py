from django.shortcuts import redirect, render

from .models import *
from .forms import *


def product_view(request):
    if request.method == "POST":
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("products")
        return redirect("products")
    
    products = Product.objects.all().order_by("-id")
    context = {
        "products": products,
    }
    return render(request, "product/products.html", context)


def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product,
    }
    return render(request, "product/product_detail.html", context)