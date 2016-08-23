from modeltranslation.translator import translator, TranslationOptions

from models import ProjectType, Project, AuthorRole


class ProjectTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'name_plural', 'slug')

translator.register(ProjectType, ProjectTypeTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'text_header', 'slug', 'history_text')

translator.register(Project, ProjectTranslationOptions)


class AuthorRoleTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(AuthorRole, AuthorRoleTranslationOptions)
