from django.conf import settings
from django.db import models


class WorldShare(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    world = models.ForeignKey("World", on_delete=models.CASCADE)

    can_create_characters = models.BooleanField(default=False)
    can_create_stories = models.BooleanField(default=False)
    can_edit_world = models.BooleanField(default=False)
