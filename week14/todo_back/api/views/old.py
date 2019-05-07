from django.shortcuts import render
from django.http import JsonResponse
from ..serializers import TaskSerializer, ListSerializer,ListSerializer2
from django.views.decorators.csrf import csrf_exempt
from ..models import TaskList,Task
import json
# Create your views here.


@csrf_exempt
def lists(request):
    if request.method == 'GET':
        all_lists = TaskList.objects.all()
        # json_lists=[l.to_json() for l in all_lists]
        ser=ListSerializer(all_lists,many=True)
        return JsonResponse(ser.data, safe=False,status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        # li=TaskList()
        # li.name=data.get('name','')
        # li.save()
        ser=ListSerializer2(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
        return JsonResponse(ser.errors)

@csrf_exempt
def task_list_detail(request,pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)},safe=False)
    if request.method=='GET':
        #json_li=li.to_json()
        ser=ListSerializer(li)
        return JsonResponse(ser.data,status=200)
    elif request.method=="PUT":
        data=json.loads(request.body)
        # li.name=data.get('name',li.name)
        # li.save()
        ser=ListSerializer(instance=li,data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=200)
        return JsonResponse(ser.errors)
    elif request.method=='DELETE':
        li.delete()
        return JsonResponse({},status=204)

@csrf_exempt
def list_tasks(request,pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method =='GET':
        tasks = list.task_set.all()
        ser = TaskSerializer(tasks, many=True)
        return JsonResponse(ser.data, safe=False,status=200)
    elif request.method=='POST':
        data=json.loads(request.body)
        print(data)
        ser=TaskSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=200)
        return JsonResponse(ser.errors)


