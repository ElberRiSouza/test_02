from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    link = models.URLField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title