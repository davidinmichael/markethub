from django.shortcuts import redirect, render

from .models import *
from .forms import *


def product_view(request):
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        if form.is_valid():
            form.save(owner=request.user)
            return redirect("products")
        return redirect("products")
    
    products = Product.objects.all().order_by("-id")
    context = {
        "products": products,
    }
    return render(request, "product/products.html", context)