from django.conf.urls import url

from . import views

app_name = 'imgboard'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^thread(?P<thread_id>[0-9]+)/$', views.ThreadView.as_view(), name='thread')
]
