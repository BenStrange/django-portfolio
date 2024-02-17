from django.urls import path
from . import views

urlpatterns = [
    path("jobs/<int:pk>", views.JobDetailView.as_view(), name="detail"),
    path("jobs/summary/", views.JobSummary.as_view(), name="summary"),
]
