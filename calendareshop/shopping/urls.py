from django.conf.urls import include, patterns, url
from django.shortcuts import redirect

from views import shop


urlpatterns = patterns('',
    url(r'', include(shop.urls)),
    url(r'^products/$', 'shopping.views.product_list', name='plata_product_list'),
    url(r'^products/(?P<object_id>\d+)/$', 'shopping.views.product_detail', name='plata_product_detail'),

    url(r'^reporting/', include('plata.reporting.urls')),
)
