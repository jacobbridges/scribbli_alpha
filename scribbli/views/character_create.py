from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse

from scribbli.models import Character, World


class CharacterCreateView(LoginRequiredMixin, CreateView):
    template_name = 'universe/character-create.html'
    model = Character
    fields = ['name', 'description']

    @property
    def world(self):
        if hasattr(self, '_world') and getattr(self, '_world') is not None:
            pass
        else:
            world_id = self.kwargs.get('pk')
            setattr(self, '_world', World.objects.get(pk=world_id))
        return getattr(self, '_world')

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({'world': self.world})
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.home_world = self.world
        form.instance.current_world = self.world
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'universe_character_detail',
            kwargs={'pk': self.object.pk}
        )
