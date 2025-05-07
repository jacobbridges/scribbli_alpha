from django.conf import settings
from django.db import models

from scribbli import constants


class Thread(models.Model):
    class Kind(models.TextChoices):
        STORY = constants.STORY_THREAD, "Story"
        TALK = constants.TALK_THREAD, "Talk"

    name = models.CharField(default="", blank=True, max_length=100)
    is_pinned = models.BooleanField(default=False)
    kind = models.CharField(max_length=2, choices=Kind.choices)

    # system fields
    system_name = models.CharField(default="", blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relations
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="threads", on_delete=models.CASCADE)
    story = models.ForeignKey("Story", null=True, related_name="threads", on_delete=models.SET_NULL)


class StoryThreadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=constants.STORY_THREAD)


class StoryThread(Thread):
    objects = StoryThreadManager()

    class Meta:
        proxy = True


class TalkThreadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(kind=constants.TALK_THREAD)


class TalkThread(Thread):
    objects = TalkThreadManager()

    class Meta:
        proxy = True
