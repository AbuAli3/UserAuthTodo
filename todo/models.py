from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(null=True, blank=True)  # Allow null values
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
