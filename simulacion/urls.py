from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', proyecto.views.index, name='index'),
    url(r'^', include('proyecto.urls')),
]
