"""
URLs
"""
# pylint: disable=invalid-name, unused-import
from django.conf.urls import url, include
from . import views

urlpatterns = [\
    url(r'^', views.view),
]
