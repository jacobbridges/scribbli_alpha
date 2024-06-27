from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from scribbli.models import World


class WorldDetailView(LoginRequiredMixin, DetailView):
    model = World
    template_name = 'universe/world-detail.html'
