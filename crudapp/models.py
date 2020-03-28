from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Todo(models.Model):
    text = models.CharField(max_length=80)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    def __str__(self):
        print(self.user)
        return self.text
