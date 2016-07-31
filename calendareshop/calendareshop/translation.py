from modeltranslation.translator import translator, TranslationOptions

from models import ProjectType, Project, AuthorRole


class ProjectTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'name_plural', 'slug')

translator.register(ProjectType, ProjectTypeTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'slug')

translator.register(Project, ProjectTranslationOptions)


class AuthorRoleTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(AuthorRole, AuthorRoleTranslationOptions)
