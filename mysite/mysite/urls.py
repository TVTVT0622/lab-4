from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^index/$','book.views.index'),
    url(r'^search/$','book.views.search'),
    url(r'^detail/$','book.views.detail'),
	url(r'^delete/$','book.views.delete'),
    url(r'^show_book/$','book.views.show_book'),
    url(r'^show_author/$','book.views.show_author'),
 )