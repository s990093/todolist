from django.urls import path

from .TaskCreateAPIView import TaskCreateAPIView

from .views import *

app_name = 'App'


urlpatterns = [
    path('task-status/', TaskStatusAPI.as_view(), name='task-status'),
    path('tasks/', TaskCreateAPIView.as_view(), name='task-create'),
    # path('classifier/', TaskClassifier.as_view(), name='task-classifier'),

]
