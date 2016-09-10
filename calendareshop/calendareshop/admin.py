# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from adminsortable.admin import SortableAdmin, SortableTabularInline, NonSortableParentAdmin

from .widgets import URLFileInput
from .models import Project, ProjectType, ProjectImage, \
    Author, AuthorRole, NewsletterSubscription, History, \
    StaticPage


class AdminImageWidget(URLFileInput):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            output.append('<img src="{}">'.format(value.url))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class GalleryImageForm(forms.ModelForm):
    """
    Image Admin Form
    """
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
