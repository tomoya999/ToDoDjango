from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # todo = models.ForeignKey(
    #     'crudapp.Todo',
    #     null=True,
    #     on_delete=models.PROTECT
    #     )
    # def __str__(self):
    #     print(self.todo)
        pass
