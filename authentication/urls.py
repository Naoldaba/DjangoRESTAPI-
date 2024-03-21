from django.urls import re_path
from authentication import views

urlpatterns=[
    re_path(r'^register/$', views.RegisterAPIView.as_view(), name='register'),
    re_path(r'^login/$', views.LoginAPIView.as_view(), name='login'),
    re_path(r'^user/$', views.AuthUserAPIView.as_view(), name='user')
]
