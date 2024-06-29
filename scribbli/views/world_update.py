from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from scribbli.models import World
from scribbli.views.mixins import IsOwnerMixin


class WorldUpdateView(LoginRequiredMixin, IsOwnerMixin, UpdateView):
    template_name = 'universe/world-update.html'
    model = World
    fields = ['name', 'visibility']
    context_object_name = 'world'

    def get_success_url(self):
        return reverse(
            'universe_world_detail',
            kwargs={'pk': self.object.pk}
        )
