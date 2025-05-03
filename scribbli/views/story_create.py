from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse

from scribbli.models import Story, World, StoryThread


class StoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'universe/story-create.html'
    model = Story
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
        form.instance.world = self.world
        result = super().form_valid(form)
        # Create the two default threads that every story should have
        StoryThread.objects.create(
            name="Main",
            system_name="main",
            story=self.object,
        )
        StoryThread.objects.create(
            name="OOC",
            system_name="ooc",
            story=self.object,
        )
        return result


    def get_success_url(self):
        return reverse(
            'story_detail',
            kwargs={'pk': self.object.pk}
        )
