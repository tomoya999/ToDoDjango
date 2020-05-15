from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from users.models import CustomUser

class Todo(models.Model):
    text = models.CharField(max_length=80)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
        )
    def __str__(self):
        return self.text
