from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=60)
    note = models.CharField(max_length=2000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title.capitalize()
