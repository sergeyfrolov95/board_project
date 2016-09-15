from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^board/', include('imgboard.urls')),
    url(r'^admin/', admin.site.urls),
]
