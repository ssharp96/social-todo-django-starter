from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login_view/$', views.login_view, name='login_view'),
    url(r'logout_view/$', views.logout_view, name='logout_view'),
    url(r'register_view/$', views.register_view, name='register_view'),
]

