from django.conf.urls import url
from . import views
from accounts import views

urlpatterns=[
        url(r'^$', views.home)

]