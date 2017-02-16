from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.crawl_image, name='crawl_image'),
]
