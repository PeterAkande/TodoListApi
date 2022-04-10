from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='akandepeter86@gmail.com')

    def __str__(self):
        return self.title
