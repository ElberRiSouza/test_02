from django.db import models

from tinymce import models as tinymce_models

class Member(models.Model):
    name = models.CharField(max_length=200)
    introduction_text = tinymce_models.HTMLField()
    member_image = models.ImageField(blank=True)
    linkedin = models.URLField(max_length=600, blank=True, null=False)
    orcid = models.URLField(max_length=600, blank=True, null=False)
    

    def __str__(self):
        return self.name


class Former_member(models.Model):
    name = models.CharField(max_length=200)
    introduction_text = models.TextField()
    member_image = models.ImageField(blank=True)
    linkedin = models.URLField(max_length=600, blank=True, null=False)
    orcid = models.URLField(max_length=600, blank=True, null=False)
    

    def __str__(self):
        return self.name
