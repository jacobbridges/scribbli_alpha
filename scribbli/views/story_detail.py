from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from scribbli.models import Story


class StoryDetailView(LoginRequiredMixin, DetailView):
    model = Story
    template_name = 'universe/story-detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({
            'is_owner': self.object.owner == self.request.user,
        })
        return kwargs
