from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from .models import Voter, VotedImage, Season


def vote(request, email, hash):
    voter = Voter.check_and_get_voter(email, hash)
    if voter is None:
        raise PermissionDenied
    active_season = request.GET.get('season', Season.INTRO)
    return render(request, 'voting/vote.html', {
        'voter': voter,
        'voted_images': VotedImage.objects.all(),
        'seasons': Season.CHOICES,
        'active_season': request.GET.get('season', Season.INTRO),
        'active_season_name': Season.get(active_season),
        'month_dict': Season.months_dict(),
    })
