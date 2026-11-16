from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    title = models.CharField(max_length=127)
    summary = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    thumbnail = models.URLField()
    textbody = models.TextField()
    views = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title