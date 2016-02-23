from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tasks, name='tasks'),
    url(r'^create/', views.create, name='create'),
    url(r'^delete/([0-9]+)', views.delete, name='delete'),
    url(r'^toggle/([0-9]+)', views.toggle, name='toggle')

]

