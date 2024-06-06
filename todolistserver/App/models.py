from django.db import models
from rest_framework import serializers

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    time = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=6, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    deadline = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, null=True, blank=True)

class BaseTask(models.Model):
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

class ClassifyTask(BaseTask):
    category = models.CharField(max_length=100)

class TaskCompletion(BaseTask):
    subject = models.CharField(max_length=100)

class LongTermGoal(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_date = models.DateTimeField()
    progress = models.IntegerField()



# se

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'