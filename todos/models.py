from django.db import models

# Create your models here.

class TodoTable(models.Model):
    content = models.TextField(max_length=100)

    def __str__(self):
        return self.content