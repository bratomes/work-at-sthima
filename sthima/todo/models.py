from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Stores a single task, related to :model:`auth.User`
    """
    position = models.IntegerField()
    description = models.CharField(max_length=80)
    done = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """
        String representation of a task
        """
        return self.description
