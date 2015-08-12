from django.db import models
from django.db.models.aggregates import Count

from random import randint

# Create your models here.

class StoryManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('_id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

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
    summary = models.TextField()
    text = models.TextField(blank=True, default='')
    title = models.CharField(max_length=2000)
    url = models.CharField(max_length=2000)
    #selected = models.BooleanField()
    objects = StoryManager()

class Coder(models.Model):
    coder_name = models.CharField(max_length=100)
    coder_id = models.IntegerField()


class StoryCoding(models.Model):
    story_id = models.IntegerField(default=-10)
    coder_id = models.IntegerField()
    coder_coding = models.IntegerField() #control

    
