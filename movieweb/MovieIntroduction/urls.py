from django.conf.urls import url
from MovieIntroduction import views


urlpatterns = [
    url(r'^$', views.MovieIntroduction, name='MovieIntroduction'),
]