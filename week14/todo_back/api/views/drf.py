
from ..serializers import ListSerializer2,TaskSerializer
from ..models import TaskList,Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def lists(request):
    if request.method == 'GET':
        all_lists = TaskList.objects.all()
        # json_lists=[l.to_json() for l in all_lists]
        ser=ListSerializer2(all_lists,many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        ser=ListSerializer2(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT','DELETE'])
def task_list_detail(request,pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        ser=ListSerializer2(li)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        ser=ListSerializer2(instance=li,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    elif request.method=='DELETE':
        li.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','PUT'])
def list_tasks(request,pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        tasks = list.task_set.all()
        ser = TaskSerializer(tasks, many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method=="POST":
        TaskSerializer.listik=list
        ser=TaskSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors)


