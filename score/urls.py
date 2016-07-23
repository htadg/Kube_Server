from django.conf.urls import url

from .views import PlayerList

urlpatterns = [
    url(r'^v1/score/$', PlayerList.as_view()),
]