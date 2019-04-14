from django.urls import path
from . import views

urlpatterns=[
    path('task_lists/',views.lists),
    path('task_lists/<int:pk>/',views.task_list_detail),
    path('task_lists/<int:pk>/tasks/',views.list_tasks),

]