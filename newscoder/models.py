from django.db import models
from django.db.models.aggregates import Count

from random import randint

# Create your models here.
#SQLITE QUERY TO RANDOM SAMPLE
#sqlite> update newscoder_story set selected = abs(random()) < 1000 * 9223372036854775807 / 99166 where publication <> 'Twitte#r';
import logging
logger = logging.getLogger(__name__)

class StoryManager(models.Manager):
    def random_uncoded_by(self, coder_id):
        '''
        This took a lot of time because we need to get info from two tables
        We use the related_model to do this, they use the __, which is one use of this.
        The idea is that there is rich language to construct SQL queries
        There is two levels of this language. THere are methods that you can call on the model
        managers like 'filter, counter' Python object methods. Then there is another layer of language
        which allows you to choose a comparison operator and field or related models bi-directionally
        '''
        selected_stories = self.filter(selected=True)
        possibilities = selected_stories.exclude(storycoding__coder_id=coder_id)
                
        count = possibilities.count()

        logger.error("Count was %d" % count)
        
        random_index = randint(0, count - 1)
        return possibilities[random_index]

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
    selected = models.BooleanField(default=False)
    objects = StoryManager()

## class Coder(models.Model):
##     coder_name = models.CharField(max_length=100)
##     coder_id = models.IntegerField(primary_key=True)

class StoryCoding(models.Model):
    story = models.ForeignKey(Story) #django adds "_id" in sql schema
    coder_id = models.CharField(max_length=100)
    coder_coding = models.IntegerField() #control
