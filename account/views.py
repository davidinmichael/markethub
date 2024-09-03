from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *
from .forms import *


class Index(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, "account/index.html")


def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        print("Post request")
        if login_form.is_valid():
            email = login_form.cleaned_data["email"]
            password = login_form.cleaned_data["password"]
            print(f"Email: {email}, Password: {password}")

            try:
                account = Account.objects.get(email=email)
            except Account.DoesNotExist:
                context = {
                    "message": "Invalid email address.",
                }
                return render(request, "account/login.html", context)
            
            if account.check_password(password):
                account_serializer = AccountSerializer(account).data
                print(f"User: {account_serializer}")
                context = {
                    "user": account_serializer,
                }
                return render(request, "account/index.html", context)
            return render(request, "account/login.html")
        return render(request, "account/login.html")
    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {
            "message": "User with this email already exist",
        }
        return render(request, "account/register.html", context)
    return render(request, "account/register.html")
            
