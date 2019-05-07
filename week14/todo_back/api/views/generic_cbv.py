from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters
from ..filters import TaskFilter
from ..models import TaskList,Task,TaskListManager
from django.contrib.auth.models import User
from ..serializers import TaskListSerializer2, UserSerializer,TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class TasksFromList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    filter_backends =(DjangoFilterBackend, SearchFilter,OrderingFilter)
    # filterset_fields=('name','status')
    #week14
    filter_class=TaskFilter

    # pagination_class = LimitOffsetPagination
    ordering_fields=('name','id',)
    ordering=('name',)


    def get_queryset(self):
        try:
            t=TaskList.objects.get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise
        queryset=t.tasks.all()
        return queryset

class Lists2(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    http_method_names = ['get']


class Lists(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)
    # week14
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2



