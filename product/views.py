from django.shortcuts import redirect, render
from django.http import HttpResponse

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
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            products = cart.products.all()
        except Cart.DoesNotExist:
            products = []
    context = {
        "product": product,
        "products": products,
    }
    return render(request, "product/product_detail.html", context)


def add_to_cart(request):
    print("Add to Cart")
    if request.method == "POST":
        print("Add to cart Post request")
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)

        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)
        mod_cart = cart.products.add(product)
        return HttpResponse(status=204)

    