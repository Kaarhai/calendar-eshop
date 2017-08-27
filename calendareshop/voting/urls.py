from django.conf.urls import include, patterns, url


urlpatterns = [
    url(r'^vote/(?P<email>[\w@._]+)/(?P<hash>\w+)/$', 'voting.views.vote', name='voting_vote'),
    url(r'results/', 'voting.views.results', name='voting_results'),
]
