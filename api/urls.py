from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^restaurants', views.get_nearby_places, name='places'),
]