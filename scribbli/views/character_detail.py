from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from scribbli.models import Character


class CharacterDetailView(LoginRequiredMixin, DetailView):
    model = Character
    template_name = 'universe/character-detail.html'
    context_object_name = 'character'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({
            'is_owner': self.object.owner == self.request.user,
        })
        return kwargs
