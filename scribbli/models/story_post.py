from django.conf import settings
from django.db import models


class StoryPostManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("author", "thread")
            .order_by("published_at")
        ).annotate(story_id=models.F("thread__story_id"))


class StoryPost(models.Model):
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="story_posts", on_delete=models.CASCADE)
    thread = models.ForeignKey("StoryThread", related_name="posts", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", related_name="posts", on_delete=models.CASCADE)

    objects = StoryPostManager()

    def __repr__(self):
        return f"<StoryPost[{self.id}] by @{self.author.username} - {self.content[0:20]}>"
