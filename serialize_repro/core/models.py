from django.db import models
from django.contrib.auth import get_user_model

class TestModel(models.Model):
    users = models.ManyToManyField(get_user_model())
