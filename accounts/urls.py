from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from accounts import views

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),

]
