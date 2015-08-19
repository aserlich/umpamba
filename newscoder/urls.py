from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    #url(r'^login$', views.login_view, name = 'login'),
    url(r'^story/(?P<story_id>ObjectId\(.*\))?/?(?P<error>.*)?$', views.story, name = 'story'),
    url(r'^postdb$', views.post, name = 'post'),
    url('^', include('django.contrib.auth.urls'))
    ]
    
