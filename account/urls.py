from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("", Index.as_view(), name="home"),
    # path("login/", LoginView.as_view(), name="login"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
]
