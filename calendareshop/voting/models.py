# -*- coding: utf-8 -*-
import hashlib
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


class Voter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    author = models.OneToOneField('calendareshop.Author', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @staticmethod
    def get_voter_hash_from_email(email):
        hashed = hashlib.sha1()
        hashed.update(settings.SECRET_KEY)
        hashed.update(email)
        hashed.update('Who is best p0ny?')
        return hashed.hexdigest()

    @classmethod
    def check_and_get_voter(cls, email, hash):
        control_hash = cls.get_voter_hash_from_email(email)
        if control_hash == hash:
            try:
                return cls.objects.get(email=email)
            except cls.DoesNotExist:
                pass
        return None

    def get_voter_link(self):
        hashed = self.get_voter_hash_from_email(self.email)
        return "%s://kalendar.%s%s" % (
            settings.SITE_PROTOCOL,
            settings.SITE_DOMAIN,
            reverse('voting_vote', args=(self.email, hashed))
        )


class Season:
    INTRO = 'intro'
    SPRING = 'spring'
    SUMMER = 'summer'
    AUTUMN = 'autumn'
    WINTER = 'winter'
    CHOICES = (
        (INTRO, 'úvod'),
        (SPRING, 'jaro'),
        (SUMMER, 'léto'),
        (AUTUMN, 'podzim'),
        (WINTER, 'zima'),
    )


class Month:
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUN = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
    CHOICES = (
        (JANUARY, 'leden'),
        (FEBRUARY, 'únor'),
        (MARCH, 'březen'),
        (APRIL, 'duben'),
        (MAY, 'květen'),
        (JUN, 'červen'),
        (JULY, 'červenec'),
        (AUGUST, 'srpen'),
        (SEPTEMBER, 'září'),
        (OCTOBER, 'říjen'),
        (NOVEMBER, 'listopad'),
        (DECEMBER, 'prosinec'),
    )


class VotedImage(models.Model):
    image = models.ImageField(upload_to='voted_images/')
    season = models.CharField(max_length=6, choices=Season.CHOICES)

    author = models.ForeignKey('calendareshop.Author', related_name='images')

    def __unicode__(self):
        return '%s: %s' % (self.author, self.image.name)


class Vote(models.Model):
    season = models.CharField(max_length=6, choices=Season.CHOICES)
    month = models.PositiveIntegerField(choices=Month.CHOICES)

    image = models.ForeignKey(VotedImage, related_name='votes')
    voter = models.ForeignKey(Voter, related_name='votes')

    def __unicode__(self):
        return "Vote from %s for %s" % (self.voter, self.image)
