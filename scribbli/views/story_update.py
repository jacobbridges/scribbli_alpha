from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from scribbli.models import Story
from scribbli.views.mixins import IsOwnerMixin


class StoryUpdateView(LoginRequiredMixin, IsOwnerMixin, UpdateView):
    template_name = 'universe/story-update.html'
    model = Story
    fields = ['name', 'description']
    context_object_name = 'story'

    def get_success_url(self):
        return reverse(
            'story_detail',
            kwargs={'pk': self.object.pk}
        )
