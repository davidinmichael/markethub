from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import *



class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            try:
                account = Account.objects.get(email=email)
            except Account.DoesNotExist:
                context = {
                    "message": "Invalid email address.",
                }
                return render(request, "account/login.html", context)
            
            if account.check_password(password):
                account_serializer = AccountSerializer(account).data
                context = {
                    "user": account_serializer,
                }
                return render(request, "account/index.html", context)
            return render(request, "account/login.html")
        return render(request, "account/login.html")
            
