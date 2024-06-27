from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'user/home.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        kwargs.update({
            'user_worlds': user.worlds.all(),
            'user_worlds': user.stories.all(),
            'user_characters': [], # TODO: Update when characters are a thing.
        })
        return kwargs