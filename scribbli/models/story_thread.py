from django.db import models

from scribbli.models.story import Story


class StoryThread(models.Model):
    name = models.CharField(max_length=100)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='threads')

    def __repr__(self):
        return f'<StoryThread[{self.id}] on {self.story}>'
