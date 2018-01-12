from django.conf.urls import url
from MovieEquipment import views


urlpatterns = [
    url(r'^$', views.MovieEquipment, name='MovieEquipment'),
]