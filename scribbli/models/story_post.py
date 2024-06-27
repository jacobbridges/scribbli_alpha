from django.conf import settings
from django.db import models


class StoryPost(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __repr__(self):
        return f"<StoryPost[{self.id}] by @{self.author.username} - {self.content[0:20]}>"
