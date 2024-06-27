from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from scribbli.models import World


class WorldListView(LoginRequiredMixin, ListView):
    model = World
    template_name = 'universe/world-list.html'
    context_object_name = 'worlds'
