from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MyPartialCharacterListView(LoginRequiredMixin, TemplateView):
    purpose = None  # Custom attribute (see urls.py)

    def get_template_names(self):
        if self.purpose == 'select':
            return ['_partials/my-character-select.html']
        return ['_partials/my-character-list.html']

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({'characters': self.request.user.characters.all()})
        return kwargs
