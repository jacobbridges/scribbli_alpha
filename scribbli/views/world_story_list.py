from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from scribbli.models import World, Story


class WorldStoryListView(LoginRequiredMixin, ListView):
    model = Story
    context_object_name = 'stories'
    template_name = 'universe/world-story-list.html'

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

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(world=self.world)
