from ..models import TaskList,Task
from ..serializers import ListSerializer2,TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



class Lists(APIView):
    def get(self, request):
        lists = TaskList.objects.all()
        serializer = ListSerializer2(lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskListDetail(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        list = self.get_object(pk)
        serializer = ListSerializer2(list)
        return Response(serializer.data)

    def put(self, request, pk):
        list = self.get_object(pk)
        serializer = ListSerializer2(instance=list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        list = self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListTasks(APIView):

    def get(self, request, pk):
        try:
            list= TaskListDetail.get_object(self,pk=pk)
        except TaskList.DoesNotExist:
            raise Http404
        tasks=Task.objects.filter(task_list=list)

        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)



