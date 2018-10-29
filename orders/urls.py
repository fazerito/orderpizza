from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^menu/$', views.menu, name="menu"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.pizza_detail,
        name='pizza_detail'),
    url(r'^about/$', views.about, name="about"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login_user, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',
        password_reset_confirm, name='password_reset_confirm'),
    #url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
    #                                       name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),


]
