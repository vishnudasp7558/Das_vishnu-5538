from django.db import models

# Create your models here.

class Task(models.Model):
    task_name=models.CharField(max_length=20)
    task_desc = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.task_name