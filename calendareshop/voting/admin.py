# -*- coding: utf-8 -*-
import datetime
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django import forms

from .models import Voter, VotedImage, Vote
from common.widgets import AdminImageWidget


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
        })

        send_mail(
            'Kalendář Draci.info: Hlasování začalo',
            msg_plain,
            settings.DEFAULT_FROM_EMAIL,
            [voter.email],
            fail_silently=False
        )
email_voters.short_description = "Send email to all voters that voting started"


class VoterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    actions = [email_voters]


class VotedImageAdmin(admin.ModelAdmin):
    form = GalleryImageForm
    list_display = ['image', 'season', 'author', 'date_created']


admin.site.register(Voter, VoterAdmin)
admin.site.register(VotedImage, VotedImageAdmin)
admin.site.register(Vote)
