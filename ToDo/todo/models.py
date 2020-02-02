from django.db import models

# Create your models here.

# 優先度の定義 （左がソースでの名称 右が画面上での名称）
PRIORITY = (('danger','high'),('info','normal'),('success','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title