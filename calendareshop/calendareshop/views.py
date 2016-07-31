# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.shortcuts import render
from django.http import Http404

from models import Project


def index(request):
    project = Project.objects.enabled().first()
    return render(request, "calendareshop/index.html", {'project': project})


class OrderItemForm(forms.Form):
    quantity = forms.IntegerField(label=('quantity'), initial=1,
        min_value=1, max_value=100)


def project(request, slug):
    is_current_project = False
    project = None
    if not slug:
        project = Project.objects.enabled().first()
        is_current_project = True
    else:
        for lang_code, _ in settings.LANGUAGES:
            filters = {'slug_%s' % lang_code: slug}
            try:
                project = Project.objects.enabled().get(**filters)
                if project == Project.objects.enabled()[0]:
                    is_current_project = True
            except Project.DoesNotExist:
                pass
                # try different language

    if not project:
        raise Http404("No project found.")

    products = project.products.all()
    for product in products:
        product.form = OrderItemForm()
    return render(request, "calendareshop/index.html", {
        'project': project,
        'products': products,
        'is_current_project': is_current_project
    })
