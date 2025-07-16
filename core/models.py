from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # on del mtlb jab user del ho tu uska records b del ho jaien
    # foreignkey = many to one yani jab hum chahty hyn k like task, assignment,post, order etc sab ak user k sath linked hon

    def __str__(self):
        return self.title
