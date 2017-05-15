from django.conf.urls import url

from . import views

app_name = 'oddsboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<block_height>[0-9]+)/$', views.detail, name='detail')
]
