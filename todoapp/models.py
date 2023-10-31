from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
