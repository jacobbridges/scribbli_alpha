from django.db import models

from scribbli.models.character import Character
from scribbli.models.story import Story


class StatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    APPROVED = 'APPROVED', 'Approved'
    DENIED = 'DENIED', 'Denied'


class StoryCharacterJoinRequest(models.Model):
    STATUS_CHOICES = StatusChoices

    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='join_requests')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='join_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('character', 'story'),)
