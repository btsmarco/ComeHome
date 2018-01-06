from django.conf.urls import include, url
from django.views.generic.base import RedirectView

urlpatterns = [
    url('', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
]
