from django.db import models


class StoryThreadManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .order_by("id")
        )


class StoryThread(models.Model):
    name = models.CharField(max_length=100)
    system_name = models.CharField(default="", blank=True, max_length=100)
    story = models.ForeignKey("Story", on_delete=models.CASCADE, related_name='threads')

    objects = StoryThreadManager()

    class Meta:
        unique_together = (("story", "system_name"), ("story", "name"))

    def __repr__(self):
        return f'<StoryThread[{self.id}] on {self.story}>'
