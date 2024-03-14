from django.db import models
from tinymce import models as tinymce_models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    image = models.ImageField(blank=True)
    

    def __str__(self):
        return self.title
