from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=60)
    context = models.CharField(max_length=500)
    def __str__(self):
        return self.title