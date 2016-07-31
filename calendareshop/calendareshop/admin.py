# -*- coding: utf-8 -*-
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from models import Project, ProjectType, ProjectImage, Author, AuthorRole


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
