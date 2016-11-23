# -*- coding: utf-8 -*-

from django.conf.urls import url

from views import SitemapView


urlpatterns = [
    url(r'^', SitemapView.as_view()),
]
