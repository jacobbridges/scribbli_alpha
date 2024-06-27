from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from scribbli.models import World


class WorldDetailView(LoginRequiredMixin, DetailView):
    model = World
    template_name = 'universe/world-detail.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({
            'is_owner': self.object.owner == self.request.user,
        })
        return kwargs
