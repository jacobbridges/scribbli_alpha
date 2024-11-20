from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from scribbli.models import Story


class StoryListView(LoginRequiredMixin, ListView):
    model = Story
    template_name = 'universe/story-list.html'
    context_object_name = 'stories'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(visibility=Story.VISIBILITY_CHOICES.PUBLIC)
        return qs
