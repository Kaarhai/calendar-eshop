# -*- coding: utf-8 -*-
import datetime
from collections import OrderedDict

from django.shortcuts import render
from django.db.models import Count
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Voter, VotedImage, Season, Vote, Month


def vote(request, email, hash):
    voter = Voter.check_and_get_voter(email, hash)
    if voter is None:
        raise PermissionDenied

    own_seasons = []
    own_images = VotedImage.objects.filter(authors__voter__in=[voter])
    for image in own_images:
        own_seasons.append(image.season)

    # substract num of months of season that have voter image in it
    required_count = 13
    season_dict = dict(Season.CHOICES_MONTHS)
    for own_season in own_seasons:
        required_count -= len(season_dict[own_season])

    # find first active season
    active_season = ''
    for season, _ in Season.CHOICES:
        if season not in own_seasons:
            active_season = request.GET.get('season', season)
            break

    errors = []
    votes = {}
    voting_finished = False
    if request.method == 'POST':
        voter.votes.all().delete()
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
            if image.season in own_seasons:
                # cannot vote in season with own image
                continue
            # check if there is only one vote for one image
            if image in votes.values():
                continue
            Vote.objects.get_or_create(
                season=image.season,
                month=month,
                image=image,
                voter=voter)
            votes[month] = image
        if len(votes) < required_count:
            errors.append('Nehlasovali jste pro všechny obrázky (%s zbývá). Napravte to prosím.' % (required_count - len(votes)))
            voter.voting_finished = False
        else:
            voting_finished = True
            voter.voting_finished = True
        voter.save(update_fields=['voting_finished'])

    return render(request, 'voting/vote.html', {
        'voter': voter,
        'voted_images': VotedImage.objects.exclude(votes__voter=voter),
        'votes': {vote.month: vote.image for vote in voter.votes.all()},
        'seasons': Season.CHOICES,
        'active_season': active_season,
        'month_dict': Season.months_dict(),
        'own_seasons': own_seasons,
        'errors': errors,
        'voting_finished': voting_finished,
        'voting_ended': Vote.voting_ended(),
        'voting_end_month_day': settings.VOTING_END_MONTH_DAY,
    })


@login_required
def results(request):
    # init result struct
    results = OrderedDict()
    for season, name in Season.CHOICES:
        results[season] = {}
        results[season]['season_name'] = name
    for image in VotedImage.objects.filter(date_created__year=datetime.date.today().year, votes__voter__voting_finished=True).annotate(votes_count=Count('votes')).order_by('-votes_count'):
        results[image.season].setdefault('images', [])
        month_counts = {}
        # find out most voted months
        for vote in image.votes.all():
            month_counts.setdefault(vote.month, 0)
            month_counts[vote.month] += 1
        image_months = []
        for month, count in sorted(month_counts.items(), key=lambda x: x[0]):
            image_months.append({
                'month': month,
                'month_name': Month.get(month),
                'count': count
            })
        image.image_months = image_months
        results[image.season]['images'].append(image)

    return render(request, 'voting/results.html', {
        'results': results,
    })
