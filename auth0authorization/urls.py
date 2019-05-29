from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/public$', views.public),
    url(r'^api/private$', views.private),
    url(r'^api/private-rpas$', views.private_rpas),
    url(r'^api/private-operator$', views.private_operator),
]