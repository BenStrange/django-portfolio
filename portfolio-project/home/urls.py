from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutInterfaceView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("forgotpassword/", views.ForgotPasswordView.as_view(), name="forgotpassword"),
]
