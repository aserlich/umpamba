from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Story, StoryManager

# Create your views here.

def index(request):
    story = Story.objects.random()
        
    context = {
        'plum_color': "Very very purple",
        'story_title': story.title
        }
    return render(request, 'newscoder/index.html', context)

