from django.conf.urls import url
from Movie import views


urlpatterns = [
    url(r'^NEWS/$', views.NEWS, name='NEWS'),
    url(r'^MovieEquipment/$', views.MovieEquipment, name='MovieEquipment'),
    url(r'^detailview/$', views.detailview, name='detailview'),
    url(r'^Order/$', views.Order, name='Order'),
    url(r'^MovieIntroduction/(?P<articleId>[0-9]+)/$', views.MovieIntroduction, name='MovieIntroduction'),
    url(r'^MovieLike/(?P<articleId>[0-9]+)/$', views.MovieLike, name='MovieLike'),
]