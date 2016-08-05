# -*- coding: utf-8 -*-
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from models import Project, ProjectType, ProjectImage, Author, AuthorRole, NewsletterSubscription


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0


class ProjectAdmin(TranslationAdmin):
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
