from ..models import TaskList,Task,TaskListManager
from django.contrib.auth.models import User
from ..serializers import ListSerializer2, UserSerializer,TaskSerializer2
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class Lists2(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = ListSerializer2
    http_method_names = ['get']


class Lists(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def get_serializer_class(self):
        return ListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = ListSerializer2
