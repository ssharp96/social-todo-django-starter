from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # id = models.UUIDField(primary_key = True, default=uuid.uuid4(), editable=False)
    owner = models.ForeignKey(User, related_name="owned_tasks")
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    is_complete = models.BooleanField(default=False)
    collaborators = models.ManyToManyField(User, related_name="tasks")

