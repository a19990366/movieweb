from django.conf.urls import url
from BuyTicket import views


urlpatterns = [
    url(r'^$', views.BuyTicket, name='BuyTicket'),
]