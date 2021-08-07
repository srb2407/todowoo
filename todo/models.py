from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class ToDo(models.Model):
    title = models.CharField(max_length=250)
    memo = models.TextField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=CASCADE)

    # show the title as the todo name
    def __str__(self):
        return self.title
