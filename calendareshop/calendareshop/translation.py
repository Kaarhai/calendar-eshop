from modeltranslation.translator import translator, TranslationOptions

from models import ProjectType, Project, AuthorRole, History, ProjectImage, StaticPage


class ProjectTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'name_plural', 'slug')

translator.register(ProjectType, ProjectTypeTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'text_header', 'slug')

translator.register(Project, ProjectTranslationOptions)


class ProjectImageTranslationOptions(TranslationOptions):
    fields = ('description', )

translator.register(ProjectImage, ProjectImageTranslationOptions)


class AuthorRoleTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(AuthorRole, AuthorRoleTranslationOptions)


class HistoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(History, HistoryTranslationOptions)


class StaticPageTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')

translator.register(StaticPage, StaticPageTranslationOptions)
