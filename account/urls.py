from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("", Index.as_view(), name="home"),
    # path("login/", LoginView.as_view(), name="login"),
    path("login/", views.login_view, name="login"),
]
