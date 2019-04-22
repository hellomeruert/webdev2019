from django.urls import path
from . import views

urlpatterns=[
    path('task_lists/',views.Lists.as_view()),
    path('task_lists/<int:pk>/',views.TaskListDetail.as_view()),
    path('task_lists/<int:pk>/tasks/',views.list_tasks),
    path('login/', views.login),
    path('logout/', views.logout),
]