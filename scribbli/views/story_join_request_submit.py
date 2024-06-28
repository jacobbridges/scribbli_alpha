from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View

from scribbli.models import Story, Character, StoryCharacterJoinRequest
from scribbli.utils.decorators import obj_as_prop


@obj_as_prop('story', Story)
class StoryJoinRequestSubmitView(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        character_id = request.POST.get('character_id')
        # TODO: Validate the character_id (must be an int - could use form for this?)

        # Ensure the character exists
        try:
            character = Character.objects.get(pk=character_id)
        except Character.DoesNotExist:
            raise Http404()

        try:
            join_req = StoryCharacterJoinRequest(
                character=character,
                story=self.story,
            )
            join_req.save()
        except IntegrityError:
            return HttpResponse(
                'You have already requested for that character to join the story.',
                content_type='text/plain',
            )
        
        return HttpResponse(
            'Your join request has been submitted.',
            content_type='text/plain',
        )


    def get(self, request, **kwargs):
        return JsonResponse({
            'name': self.story.name,
            'description': self.story.description,
        })
