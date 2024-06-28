from django.conf import settings
from django.db import models

from scribbli.models.world import World
from scribbli.models.story import Story


class Character(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='characters')
    home_world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='natives')
    current_world = models.ForeignKey(World, null=True, on_delete=models.SET_NULL, related_name='residents')
    current_story = models.ForeignKey(Story, null=True, on_delete=models.SET_NULL, related_name='characters')

    def __repr__(self):
        return f'<Character[{self.id}]>'
