from django.db import models
from myapp.models import Goal
from tag.models import Tag

# Create your models here.
class Goaltag(models.Model):
    goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('goal_id', 'tag_id')

    def __str__(self):
        return f'{self.goal_id} - {self.tag_id}'
    