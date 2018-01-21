from django.conf.urls import url
from Movie import views


urlpatterns = [
    url(r'^NEWS$', views.NEWS, name='NEWS'),
    url(r'^MovieEquipment$', views.MovieEquipment, name='MovieEquipment'),
    url(r'^OrderTicket$', views.OrderTicket, name='OrderTicket'),
    url(r'^OrderTickets$', views.OrderTickets, name='OrderTickets'),
    url(r'^MovieIntroduction/(?P<articleId>[0-9]+)/$', views.MovieIntroduction, name='MovieIntroduction'),
    url(r'^MovieLike/(?P<articleId>[0-9]+)/$', views.MovieLike, name='MovieLike'),
]