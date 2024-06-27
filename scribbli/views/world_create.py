from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from scribbli.models import World


class WorldCreateView(LoginRequiredMixin, CreateView):
    template_name = 'universe/world-create.html'
    model = World
    fields = ['name']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'universe_world_detail',
            kwargs={'pk': self.object.pk}
        )
