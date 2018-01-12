from django.conf.urls import url
from MovieTheater import views


urlpatterns = [
    url(r'^$', views.MovieTheater, name='MovieTheater'),
]