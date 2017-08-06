# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from adminsortable.admin import SortableAdmin, SortableTabularInline, NonSortableParentAdmin

from .models import Project, ProjectType, ProjectImage, \
    Author, AuthorRole, NewsletterSubscription, History, \
    StaticPage
from common.widgets import AdminImageWidget


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        widgets = {
            'image_preview': AdminImageWidget,
            'image': AdminImageWidget,
        }
        exclude = ()


class ProjectImageInline(TranslationTabularInline, SortableTabularInline):
    model = ProjectImage
    form = GalleryImageForm
    extra = 0


class ProjectAdmin(NonSortableParentAdmin, TranslationAdmin):
    inlines = [ProjectImageInline]
    filter_horizontal = ('authors',)
    save_as = True


admin.site.register(Project, ProjectAdmin)


class ProjectTypeAdmin(TranslationAdmin):
    pass

admin.site.register(ProjectType, ProjectTypeAdmin)


class AuthorRoleAdmin(TranslationAdmin):
    pass

admin.site.register(AuthorRole, AuthorRoleAdmin)

admin.site.register(Author)


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_created')
    search_fields = ('email', )

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)


class HistoryAdmin(SortableAdmin, TranslationAdmin):
    pass

admin.site.register(History, HistoryAdmin)


class StaticPageAdmin(SortableAdmin, TranslationAdmin):
    pass

admin.site.register(StaticPage, StaticPageAdmin)
