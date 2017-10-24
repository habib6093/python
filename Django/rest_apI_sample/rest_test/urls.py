
from django.conf.urls import include, url
from django.contrib import admin
from test_app import views
from rest_framework import routers



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/', views.postlist.as_view()),
]




