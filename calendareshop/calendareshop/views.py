# -*- coding: utf-8 -*-
import json
import datetime

from django import forms
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext_lazy as _

from calendareshop.models import Project, NewsletterSubscription, History, StaticPage
from shopping.models import ShippingRegion
from calendareshop.utils import get_currency_code


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=200)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        success_message = getattr(self, "success_message", False)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            if success_message:
                data['success_message'] = str(success_message)
            return self.render_to_json_response(data)
        else:
            return response


def index(request):
    project = Project.objects.enabled().first()
    return render(request, "calendareshop/index.html", {'project': project})


class OrderItemForm(forms.Form):
    quantity = forms.IntegerField(label=('quantity'), initial=1, min_value=1, max_value=100)


def project(request, slug):
    # try static pages
    filters = Q()
    for lang_code, a in settings.LANGUAGES:
        filters |= Q(**{'slug_%s' % lang_code: slug})
    page = StaticPage.objects.filter(filters).first()
    if page:
        return render(request, "calendareshop/staticpage.html", {'page': page})

    # try projects
    is_current_project = False
    project = None
    if not slug:
        project = Project.objects.enabled().first()
        is_current_project = True
    else:
        for lang_code, a in settings.LANGUAGES:
            filters = {'slug_%s' % lang_code: slug}
            try:
                project = Project.objects.enabled().get(**filters)
                if project in Project.objects.enabled()[:2]:
                    is_current_project = True
            except Project.DoesNotExist:
                pass
                # try different language

    if not project:
        raise Http404("No project found.")

    products = project.products.active()
    for product in products:
        product.form = OrderItemForm()
    return render(request, "calendareshop/index.html", {
        'project': project,
        'first_project': Project.objects.enabled().first(),
        'products': products,
        'is_current_project': is_current_project,
        'histories': History.objects.filter(project_type=project.project_type),
        'next_year': datetime.date.today().year + 1
    })


class NewsletterSubscriptionCreate(AjaxableResponseMixin, CreateView):
    model = NewsletterSubscription
    success_url = '/'  # TODO return to original url
    success_message = _("You are successfully subscribed!")
    fields = ['email']

    def get(self, request, *args, **kwargs):
        # just so it's not returning an error
        return HttpResponseRedirect("/")

    def form_valid(self, form):
        response = super(NewsletterSubscriptionCreate, self).form_valid(form)
        if self.request.is_ajax() and self.object.pk:
            self.object.save()
        return response


def shipping_payment(request):
    currency = get_currency_code(request)
    data = {}
    for i in range(1, 11) + [1000]:
        data.setdefault(i, [])
        for shipreg in ShippingRegion.objects.filter(shipping__name=u'Česká pošta'):
            if shipreg.quantity_min <= i <= shipreg.quantity_max:
                price = shipreg.shipping.get_shipping_price(quantity=i, currency=currency, region=shipreg.region)
                data[i].append((shipreg.region.name, price))
    return render(request, 'calendareshop/shipping_payment.html', {
        'shipping_prices': data,
        'currency': currency
    })


def resize_image(request, width, height, image):
    return redirect('/%s' % image, permanent=False)
