from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from scribbli.models import Character
from scribbli.views.mixins import IsOwnerMixin


class CharacterUpdateView(LoginRequiredMixin, IsOwnerMixin, UpdateView):
    template_name = 'universe/character-update.html'
    model = Character
    fields = ['name', 'description']
    context_object_name = 'character'

    def get_success_url(self):
        return reverse(
            'universe_character_detail',
            kwargs={'pk': self.object.pk}
        )
