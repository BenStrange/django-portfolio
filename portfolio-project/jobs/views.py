from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)
from .models import Job


class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/detail.html"
    context_object_name = "detail"


class SoonView(TemplateView):
    template_name = "jobs/soon.html"
    context_object_name = "soon"

class JobSummary(TemplateView):
    template_name = "jobs/job_summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs"] = Job.objects.all()
        return context
