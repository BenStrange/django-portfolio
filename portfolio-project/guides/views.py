from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)

# Create your views here.
class GuidesView(TemplateView):
    template_name = "guides/guides.html"
