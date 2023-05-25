from django.contrib.auth.models import User
from django.db import models


class Historic(models.Model):
    choices_type = [
        ("correction", "correction"),
        ("creation", "creation"),
        ("general", "general"),
    ]
    user = models.ForeignKey(User, related_name="historic", on_delete=models.DO_NOTHING)
    question = models.TextField(max_length=5000)
    response = models.TextField(max_length=5000)
    language = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True, blank=True)
    type = models.CharField(max_length=20, choices=choices_type, null=True)
