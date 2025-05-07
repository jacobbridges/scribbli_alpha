from django.conf import settings
from django.db import models

from scribbli import constants


class PostManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(kind=constants.IC_POST)
            .select_related("author", "thread")
            .order_by("published_at")
        )


class Post(models.Model):
    class Kind(models.TextChoices):
        IC = constants.IC_POST, "In-Character"
        TALK = constants.TALK_POST, "Talk"
        NARRATOR = constants.NARRATOR_POST, "Narrator"

    content = models.TextField()
    is_pinned = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    kind = models.CharField(max_length=2, choices=Kind.choices)

    # system fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

    # relations
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="story_posts", on_delete=models.CASCADE)
    thread = models.ForeignKey("Thread", related_name="posts", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", null=True, related_name="posts", on_delete=models.CASCADE)


class ICPostManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(kind=constants.IC_POST)
            .select_related("author", "thread", "character")
            .order_by("published_at")
        ).annotate(story_id=models.F("thread__story_id"))


class ICPost(Post):
    objects = ICPostManager()

    class Meta:
        proxy = True


class TalkPostManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(kind=constants.TALK_POST)
            .select_related("author", "thread")
            .order_by("published_at")
        )


class TalkPost(Post):
    objects = TalkPostManager()

    class Meta:
        proxy = True


class NarratorPostManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(kind=constants.NARRATOR_POST)
            .select_related("author", "thread")
            .order_by("published_at")
        ).annotate(story_id=models.F("thread__story_id"))


class NarratorPost(Post):
    objects = NarratorPostManager()

    class Meta:
        proxy = True
