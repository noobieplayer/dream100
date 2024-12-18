from django.db import models
from myapp.models import Goal

# Create your models here.
class Reminder(models.Model):
    reminder_id = models.AutoField(primary_key=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    reminder_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title