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


def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)

        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)
        mod_cart = cart.products.add(product)
        return render(request, "product/add_to_cart.html")
    return render(request, "product/add_to_cart.html")

    