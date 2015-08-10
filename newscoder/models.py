from django.db import models

# Create your models here.


class Story(models.Model):
    '''This class represents a story and the coding of story xxx'''
    author = models.CharField(max_length=2000)
    downloaded_at = models.CharField(max_length=2000)
    _id = models.CharField(max_length=2000, primary_key=True)
    meta_description = models.CharField(max_length=2000)
    owner = models.CharField(max_length=2000)
    publication = models.CharField(max_length=2000)
    published = models.CharField(max_length=2000)
    sub_type = models.CharField(max_length=2000)
    summary = models.CharField(max_length=2000)
    text = models.CharField(max_length=2000, blank=True, default='')
    title = models.CharField(max_length=2000)
    url = models.CharField(max_length=2000)

class Coder(models.Model):
    coder_name = models.CharField(max_length=100)
    coder_id = models.IntegerField()


class StoryCoding(models.Model):
    story_id = models.IntegerField(default=-10)
    coder_id = models.IntegerField()
    coder_coding = models.IntegerField() #control

    
