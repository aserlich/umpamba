from django.db import models

# Create your models here.

class Story(models.Model):
    story_text = models.CharField(max_length=2000)
    coder_code = models.IntegerField(default=-10)
