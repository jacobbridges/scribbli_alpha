from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from scribbli.views.mixins import IsOwnerMixin
from scribbli.models import Story, StoryCharacterJoinRequest
from scribbli.utils.decorators import obj_as_prop


@obj_as_prop('story', Story)
class StoryJoinRequestList(LoginRequiredMixin, IsOwnerMixin, ListView):
    model = StoryCharacterJoinRequest
    context_object_name = 'join_requests'
    template_name = 'universe/story-join-request-list.html'

    def get_object(self):
        return self.story

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({
            'story': self.story,
            'status_choices': StoryCharacterJoinRequest.STATUS_CHOICES,
        })
        return kwargs

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(story=self.story, status=StoryCharacterJoinRequest.STATUS_CHOICES.PENDING)
