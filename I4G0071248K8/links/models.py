from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    created_date = models.DateTimeField()
    active = models.BooleanField(default= True)
