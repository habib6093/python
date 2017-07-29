"""banglaidj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog_post import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',views.home),
    url(r'^post_view/(\d+)/$', views.post_view, name="post_view"),
    url(r'^delete/(\d+)/', views.delete_post, name="delete_post"),
    url(r'^new_post/', views.new_post, name="new_post"),
    url(r'^edit/(\d+)/', views.edit, name="edit"),
    url(r'^update/(\d+)/', views.update, name="update"),
]
