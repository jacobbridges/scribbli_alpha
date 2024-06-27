from django.conf import settings
from django.db import models

from scribbli.models.world import World


class Story(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stories')
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='stories')

    def __repr__(self):
        return f'<Story[{self.id}]>'
