from todos import views
from django.urls import re_path, path


urlpatterns=[
    
    re_path(r'^$', views.TodosAPIView.as_view(), name='todo'),
    path('<int:id>', views.TodoDetailAPIView.as_view(), name='todos')
]


