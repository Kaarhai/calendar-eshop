from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    url(r'^vote/(?P<email>[\w@._]+)/(?P<hash>\w+)/$', 'voting.views.vote', name='voting_vote'),
)
