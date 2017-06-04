from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.display_all_vehicles, name='display_vehicles'),
]
