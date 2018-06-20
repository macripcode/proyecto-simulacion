from django.conf.urls import url
from .views import public_page

urlpatterns = [
       url(r'^$', public_page, name='public_page'),
]
