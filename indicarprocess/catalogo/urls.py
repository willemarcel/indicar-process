# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^recursos/$',
        TemplateView.as_view(template_name='catalogo/recursos.html'),
        name='resources'),
)