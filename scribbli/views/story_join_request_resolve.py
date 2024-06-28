from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.views import View

from scribbli.models import Story, StoryCharacterJoinRequest
from scribbli.views.mixins import IsOwnerMixin
from scribbli.utils.decorators import obj_as_prop


@obj_as_prop('story', Story)
class StoryJoinRequestResolveView(IsOwnerMixin, LoginRequiredMixin, View):

    def get_object(self):
        return self.story
    def post(self, request, **kwargs):
        join_request_id = request.POST.get('join_request_id')
        status = request.POST.get('status')
        # TODO: Validate the join_request_id (must be an int - could use form for this?)
        # TODO: Validate the status is one of StoryCharacterJoinRequest.STATUS_CHOICES

        # Ensure the join request exists
        try:
            join_request = StoryCharacterJoinRequest.objects.get(pk=join_request_id)
        except StoryCharacterJoinRequest.DoesNotExist:
            raise Http404()

        join_request.status = status
        join_request.save()

        if status == StoryCharacterJoinRequest.STATUS_CHOICES.APPROVED:
            char = join_request.character
            char.current_story = self.story
            char.current_world = self.story.world
            char.save()
            verbage = 'approved'
        else:
            verbage = 'denied'
        
        return HttpResponse(
            f'You have {verbage} this join request.',
            content_type='text/plain',
        )
