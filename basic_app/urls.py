from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!

urlpatterns=[
    url('', views.index, name = 'index')
]
