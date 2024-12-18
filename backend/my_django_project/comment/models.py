from django.db import models
from myapp.models import Goal
from myapp.models import User

# Create your models here.
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content