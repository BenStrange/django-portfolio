from django.urls import path
from . import views

urlpatterns = [
    path("guides/", views.GuidesView.as_view(), name="guides"),
]