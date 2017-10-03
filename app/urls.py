from django.conf.urls import url
from .views import Top

app_name = 'top'

urlpatterns = [
    url(r'^$', Top.as_view(), name='top')
]
