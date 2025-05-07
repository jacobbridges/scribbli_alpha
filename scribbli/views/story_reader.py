from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from scribbli.models import Story, Thread


class StoryReaderView(LoginRequiredMixin, DetailView):
    model = Story
    template_name = 'universe/story-reader.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({
            'is_owner': self.object.owner == self.request.user,
            'thread_list': self.get_thread_list(),
            'current_thread': self.get_current_thread(),
            'post_list': self.get_post_list(),
            'available_character_list': self.get_available_character_list(),
            **self.get_pagination_data(),
        })
        return kwargs

    def get_thread_list(self):
        return list(self.object.threads.all())

    def get_current_thread(self):
        if thread_id := self.request.GET.get('thread_id', None):
            self._thread = Thread.objects.get(id=thread_id)
            return self._thread
        self._thread = self.object.threads.get(system_name="main")
        return self._thread

    def get_post_list(self):
        if not hasattr(self, '_thread'):
            self._thread = self.get_current_thread()
        # TODO: Handle pagination
        return self._thread.posts.all()

    def get_available_character_list(self):
        return list(self.object.characters.filter(owner=self.request.user))

    def get_pagination_data(self):
        return {
            "page_number": 1,
            "total_pages": 1,
        }
