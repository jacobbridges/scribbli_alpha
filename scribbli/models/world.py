from django.conf import settings
from django.db import models

from .world_share import WorldShare


class VisibilityChoices(models.TextChoices):
    PUBLIC = ('PUBLIC', 'Public')
    UNLISTED = ('UNLISTED', 'Unlisted')
    PRIVATE = ('PRIVATE', 'Private')


class World(models.Model):
    VISIBILITY_CHOICES = VisibilityChoices

    name = models.CharField(max_length=60)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='worlds')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, null=False, blank=False, default=VISIBILITY_CHOICES.UNLISTED)

    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_worlds', through=WorldShare)

    def __repr__(self):
        return f'<World[{self.id}]>'
