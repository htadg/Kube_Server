from django.conf.urls import url

from .views import get_score

urlpatterns = [
    url(r'^v1/get/$', get_score, name='get_score'),
]