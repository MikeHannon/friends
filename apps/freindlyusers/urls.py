from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^addFriend$', views.addFriend, name = 'createFriend'),
    url(r'^addUser$', views.addUser, name = 'createUser'),
    url(r'^showUser/(?P<id>\d+)$', views.showUser, name = 'showUser')
]
