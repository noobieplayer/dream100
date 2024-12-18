from django.db import models
from myapp.models import Goal

# Create your models here.
class Progress(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'まだ始めてないよ'),
        ('in_progress', '頑張ってるよ'),
        ('completed', '達成したよ！'),
        ('on_hold', '休憩中...'),
        ('cancelled', 'やめちゃった'),
    ]
    progress_id = models.AutoField(primary_key=True)
    goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    details = models.TextField()
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.get_status_display()}: {self.details}'