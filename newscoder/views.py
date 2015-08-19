from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login

from .models import Story, StoryManager, StoryCoding

# Create your views here.
# We know that good behavior involves "redirecting after post"
# <redirect after post> is a known web app pattern
# Every time we post we should make sure that we have properly redirected

def index(request):
    context = {
        'plum_color': "Very very purple",
        }
    return render(request, 'newscoder/index.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('story', story_id = "", error="False")
            
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...

def story(request, story_id = None, error="False"):
    story = None
    if story_id is None or story_id == "":
        story = Story.objects.random_uncoded_by(request.user.username)
    else:
        story = get_object_or_404(Story, pk = story_id)

    # we are passing the _id to index because it then needs ot be passed to post because
    # that is the only way we have to pass information around.     
    context = {
        'plum_color': "Very very purple",
        'story_title': story.title,
        'story_text': story.text,
        'story_id' : story._id,
        'error' : error == "True",
        'username' : request.user.username,
        'coder_count' : StoryCoding.objects.filter(coder_id=request.user.username).count(),
        'selected_count' : Story.objects.filter(selected=True).count()
        }
    return render(request, 'newscoder/story.html', context)

def post(request):
    # First, validate the request
    #see more about url mappings to understand how this works
    #django automatically associates the id for us so need to pass entire instance
    if request.POST.get('eleccode') is None or request.POST.get('eleccode') == "":
        return redirect('story', story_id = request.POST.get('story_id'), error="True")

    else:    
        onestory = get_object_or_404(Story, pk = request.POST.get('story_id'))
        rec = StoryCoding(story = onestory,
                          coder_id = request.user.username,
                          coder_coding = request.POST.get('eleccode')
                          )
        rec.save()
        return redirect('story', story_id = "", error="False")
                        
