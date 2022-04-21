from django.contrib.auth import get_user_model
from django.db import models

from exam_project.accounts.models import UserProfile

USER_MODEL = get_user_model()


class ProfileComments(models.Model):
    COMMENT_MAX_LENGTH = 400
    comment_text = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        USER_MODEL,
        related_name="author",
        on_delete=models.CASCADE,

    )
    receiver = models.OneToOneField(
        USER_MODEL,
        related_name="receiver",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment "{self.comment_text[:12] + "..." if len(self.comment_text) > 12 else self.comment_text} ",' \
               f' By: {self.author}, To: {self.receiver}.'
