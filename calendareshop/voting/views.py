from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from .models import Voter, VotedImage


def vote(request, email, hash):
    voter = Voter.check_and_get_voter(email, hash)
    if voter is None:
        raise PermissionDenied
    return render(request, 'voting/vote.html', {
        'voter': voter,
        'voted_images': VotedImage.objects.all()
    })
