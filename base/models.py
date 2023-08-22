from django.db import models

TASK_STATUS = (
    ("INCOMPLETE", "Incomplete"),
    ("COMPLETE", "Complete"),
    ("IN PROGRESS", "In progress"),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    status = models.CharField(max_length=15,
                  choices=TASK_STATUS,
                  default="INCOMPLETE")

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    @classmethod
    def getAllTasks(cls):
        tasks = cls.objects.all().order_by('-created')
        return tasks