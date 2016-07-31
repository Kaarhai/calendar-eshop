# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from plata.product.models import ProductBase
from plata.shop.models import PriceBase
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField


class AbstractBaseModel(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = AutoSlugField(_('slug'), populate_from='name', unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        for lang_code, lang_verbose in settings.LANGUAGES:
            if hasattr(self, 'slug_%s' % lang_code) and hasattr(self, 'name_%s' % lang_code) and getattr(self, 'slug_%s' % lang_code) == "":
                setattr(self, 'slug_%s' % lang_code, slugify(getattr(self, 'name_%s' % lang_code, u"")))
        super(AbstractBaseModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['-name']


class AuthorRole(models.Model):
    name = models.CharField(_('name'), max_length=100)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(_('name'), max_length=100)
    image = models.ImageField(upload_to="authors/")
    date_created = models.DateTimeField(auto_now_add=True)
    link_da = models.URLField(_('DeviantArt'), blank=True)
    link_web = models.URLField(_('Personal website'), blank=True)
    link_fb = models.URLField(_('Facebook'), blank=True)
    link_email = models.URLField(_('E-mail'))

    role = models.ForeignKey(AuthorRole, related_name="authors")

    def __unicode__(self):
        return self.name


class ProjectType(AbstractBaseModel):
    name_plural = models.CharField(_('plural name'), max_length=100)
    codename = models.CharField(_('project code'), max_length=50, unique=True)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.codename)


class ProjectManager(models.Manager):

    def enabled(self):
        return self.get_queryset().filter(enabled=True)


class Project(AbstractBaseModel):
    text = RichTextUploadingField()
    enabled = models.BooleanField(default=True)
    background_image = models.ImageField(upload_to="project_backgrounds/", blank=True)
    authors = models.ManyToManyField(Author, related_name="projects")

    project_type = models.ForeignKey(ProjectType, related_name="projects")

    objects = ProjectManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        lang = translation.get_language()
        return reverse("project", args=(getattr(self, 'slug_%s' % lang), ))


class ProjectImage(models.Model):
    image = models.ImageField(upload_to="projects/")
    date_created = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(Project, related_name="images")


