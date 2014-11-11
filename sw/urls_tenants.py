from django.conf.urls import patterns, url, include
from customers.views import TenantView

urlpatterns = patterns('',
    url(r'^$', TenantView.as_view()),
    url(r'^inventories/', include('inventories.urls')),
)
