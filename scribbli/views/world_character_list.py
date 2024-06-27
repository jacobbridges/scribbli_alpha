from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView

from scribbli.models import World, Character


class WorldCharacterListView(LoginRequiredMixin, ListView):
    """Powers both the native and resident listing pages."""
    model = Character
    context_object_name = 'characters'
    template_name = 'universe/world-character-list.html'
    leaf = None  # Custom attribute (see urls.py)

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
        kwargs.update({
            'leaf': self.leaf,
            'world': self.world,
        })
        return kwargs

    def get_queryset(self):
        qs = super().get_queryset()
        if self.leaf == 'natives':
            return qs.filter(home_world=self.world)
        elif self.leaf == 'residents':
            return qs.filter(current_world=self.world)
        else:
            raise Http404()
