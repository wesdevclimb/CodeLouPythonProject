"""CalorieTracker URL Configuration

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
from django.conf.urls import patterns, url
from django.contrib import admin

from CalorieTracker import views

urlpatterns = patterns('',
  url(r'^$', views.BookList.as_view(), name='book_list'),
  url(r'^new$', views.BookCreate.as_view(), name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
  url(r'^enter$', views.FoodDescriptionCreate.as_view(), name='fooddescription_new'),
  url(r'^enterread$', views.FoodDescriptionList.as_view(), name='fooddescription_list'),
  url(r'^enteredit/(?P<pk>\d+)$', views.FoodDescriptionUpdate.as_view(), name='fooddescription_edit'),
  url(r'^deleteenter/(?P<pk>\d+)$', views.FoodDescriptionDelete.as_view(), name='fooddescription_delete')
)
