from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    author_ip = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    done_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
