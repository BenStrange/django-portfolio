from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from typing import Any
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class AboutView(TemplateView):
    template_name = "about/about.html"
    context_object_name = "about"
