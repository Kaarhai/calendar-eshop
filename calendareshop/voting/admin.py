# -*- coding: utf-8 -*-
import datetime
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django import forms

from .models import Voter, VotedImage, Vote
from common.widgets import AdminImageWidget
from common.admin import ImageListAdmin


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = VotedImage
        widgets = {
            'image': AdminImageWidget,
        }
        exclude = ()


def email_voters(modeladmin, request, queryset):
    for voter in queryset:
        msg_plain = render_to_string('voting/emails/start.txt', {
            'voting_link': voter.get_voter_link(),
            'year': datetime.datetime.now().year + 1,
            'voting_end_month_day': settings.VOTING_END_MONTH_DAY,
        })

        send_mail(
            'Kalendář Draci.info: Hlasování',
            msg_plain,
            settings.DEFAULT_FROM_EMAIL,
            [voter.email],
            fail_silently=False
        )
email_voters.short_description = "Send email to all voters that voting started"


class VoterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'voting_finished']
    list_filter = ['voting_finished']
    actions = [email_voters]


class VotedImageAdmin(admin.ModelAdmin, ImageListAdmin):
    form = GalleryImageForm
    list_display = ['thumb', 'season', 'author_list', 'date_created']

    def image_name(self, obj):
        return obj.image.name

    def author_list(self, obj):
        return ", ".join(obj.authors.values_list('name', flat=True))


class VoteAdmin(admin.ModelAdmin):
    list_display = ['image_author', 'season', 'month', 'voter', 'complete_voting']
    list_filter = ['voter', 'season', 'month', 'image']

    def image_author(self, obj):
        return ", ".join(obj.image.authors.values_list('name', flat=True))

    def complete_voting(self, obj):
        return obj.voter.voting_finished


admin.site.register(Voter, VoterAdmin)
admin.site.register(VotedImage, VotedImageAdmin)
admin.site.register(Vote, VoteAdmin)
