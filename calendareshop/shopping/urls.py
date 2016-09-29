from django.conf.urls import include, patterns, url

from views import shop


urlpatterns = patterns('',
    url(r'', include(shop.urls)),
    url(r'^products/$', 'shopping.views.product_list', name='plata_product_list'),
    url(r'^products/(?P<object_id>\d+)/$', 'shopping.views.product_detail', name='plata_product_detail'),

    url(r'^email_test/(?P<order_id>\d+)/(?P<template>[\w_-]+)/$', 'shopping.views.email_test', name='email_test'),

    url(r'^reporting/', include('plata.reporting.urls')),
)
