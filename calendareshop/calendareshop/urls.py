"""calendareshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from views import project, NewsletterSubscriptionCreate, shipping_payment


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # just for localhost, processed through nginx on production
    url(r'^resize/(?P<width>-|\d+)/(?P<height>-|\d+)/(?P<image>.+)', 'calendareshop.views.resize_image'),

    url(r'^newsletter/$', NewsletterSubscriptionCreate.as_view(), name="newsletter-create"),
    url(r'^shipping_payment/$', shipping_payment, name="shipping_payment_en"),
    url(r'^doprava_platba/$', shipping_payment, name="shipping_payment_cs"),
    url(r'^$', project, {'slug': None}, name="project_index"),
    url(r'^', include('shopping.urls')),
    url(r'^voting/', include('voting.urls')),
    url(r'^(?P<slug>[\w_-]+)/$', project, name="project"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
