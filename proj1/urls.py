from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^leap/', include('leap.urls')),
    url(r'^admin/', admin.site.urls),
]