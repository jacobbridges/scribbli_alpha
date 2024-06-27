from django.conf import settings
from django.db import models


class World(models.Model):
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='worlds')

    def __repr__(self):
        return f'<World[{self.id}]>'
