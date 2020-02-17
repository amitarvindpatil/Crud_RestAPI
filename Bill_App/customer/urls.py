from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from . import views


urlpatterns = [
    re_path('customerr/(?P<pk>[0-9]+)$', views.get_delete_update_customer.as_view(),
            name='get_delete_update_customer'),
    path('customerr', views.get_post_customers.as_view(),
         name='get_post_customers')
]
