from django.conf.urls import patterns, url

from inventories import views

urlpatterns = patterns('',
    url(r'^$', views.CreateInventoryView, name='index')
)
