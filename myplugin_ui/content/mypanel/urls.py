from django.conf.urls import url

from myplugin_ui.content.mypanel import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]