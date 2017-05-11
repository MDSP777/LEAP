from django.conf.urls import url
from . import views

app_name = 'leap'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.redirect_create, name='create'),
    url(r'^submit_created_class/$', views.createClass, name='submit_created_class'),
    url(r'^view_all/$', views.viewClasses, name='view_all'),
    url(r'^view/(?P<class_id>[1-9][0-9]*)/$', views.viewSingle, name='view_single'),
    url(r'^enroll/$', views.redirect_enroll, name='enroll'),
    url(r'^submit_enrollment/$', views.enroll, name='submit_enrollment'),
]