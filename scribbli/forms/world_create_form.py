from django.forms import ModelForm

from scribbli.models import World


class WorldCreateForm(ModelForm):
    class Meta:
        model = World
        fields = ['name']
