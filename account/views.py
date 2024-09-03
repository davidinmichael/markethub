from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, login, logout

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

            # user = authenticate(request, email=email, password=password)
            user = Account.objects.get(email=email)
            if user.password == password:
                print("User is not None")
                login(request, user)
                return render(request, "account/index.html")
                
            context = {
                "message": "Invalid email address.",
            }
            return render(request, "account/login.html", context)

        return render(request, "account/login.html")
    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
        context = {
            "message": "User with this email already exist",
        }
        return render(request, "account/register.html", context)
    return render(request, "account/register.html")


def logout_view(request):
    logout(request)
    return redirect("login")



def profile_view(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "account/profile.html", context)


def change_password(request):
    user = request.user
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            new_password = form.cleaned_data["new_password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if user.password == password:
                if new_password != confirm_password:
                    return render(request, "account/profile.html")
                # user.set_password(new_password)
                user.password = new_password
                user.save()
                return redirect("login")
                
            return render(request, "account/profile.html")
    return render(request, "account/profile.html")
