from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.crawl_image, name='crawl_image'),
    url(r'^crawl_image/search/$', views.search_crawl_image, name="search_crawl_image"),
]
