from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.PageView.as_view(), name="page"),
]
