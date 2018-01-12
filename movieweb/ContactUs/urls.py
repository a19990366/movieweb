from django.conf.urls import url
from ContactUs import views


urlpatterns = [
    url(r'^$', views.ContactUs, name='ContactUs'),
]