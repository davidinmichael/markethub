from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_view, name="products"),
    path("product-detail/<int:pk>/", views.product_details, name="product_detail"),
]
