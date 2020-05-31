from django.db import models

from users.models import CustomUser


class Todo(models.Model):
    
    text = models.CharField(max_length=80)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
        )

        
    def to_dict(self):
        return {
            "id": self.id,
            "updated_at": self.updated_at,
            "text": self.text,
            "is_done": self.is_done,
            # "user": self.user,
        }

    def __str__(self):
        return self.text, self.id
