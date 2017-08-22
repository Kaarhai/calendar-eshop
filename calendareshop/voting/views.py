# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from .models import Voter, VotedImage, Season


def vote(request, email, hash):
    voter = Voter.check_and_get_voter(email, hash)
    if voter is None:
        raise PermissionDenied

    own_seasons = []
    own_images = VotedImage.objects.filter(author__voter=voter)
    for image in own_images:
        own_seasons.append(image.season)

    errors = []
    votes = {}
    if request.method == 'POST':
        # process POST data
        for selection in request.POST.getlist('selection[]'):
            parts = selection.split('-')
            try:
                image = VotedImage.objects.get(pk=parts[0])
            except VotedImage.DoesNotExist:
                continue
            month = int(parts[1])
            if 12 > month < 0:
                continue
            # check if month mathes image season
            for season, months in Season.CHOICES_MONTHS:
                if image.season == season and month not in months:
                    continue
            # check if there is only one vote for one image
            if image in votes.values():
                continue
            votes[month] = image
        if len(votes) < 13:
            # TODO update for those which cannot vote for own seasons
            errors.append('Něhlasovali jste pro všechny obrázky. Napravte to prosím.')

    active_season = request.GET.get('season', Season.INTRO)
    return render(request, 'voting/vote.html', {
        'voter': voter,
        'voted_images': VotedImage.objects.all(),
        'votes': votes or {vote.month: vote.image for vote in voter.votes.all()},
        'seasons': Season.CHOICES,
        'active_season': request.GET.get('season', Season.INTRO),
        'active_season_name': Season.get(active_season),
        'month_dict': Season.months_dict(),
        'errors': errors,
    })
